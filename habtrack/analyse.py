'''
the file analyse.py provides the basic analyse functionality to get insight into a habit, or group of habits

Imports
-------
datetime : for time mngt

Functions
---------
get_streaks(Habit)
    returns a list of lists of checkoffs e.g. [[str_1_check_1, str_1_check_2]], [str_2_check_1, str_2_check_2]]
get_longest_streak(Habit)
    returns the longest streak of a habit
get_habits_by_period(Iterable, period)
    returns a list containing the (by their periodicity) filtered habits
is_broken(habit)
    returns a bool representing if the last time period wasn checked off
get_longest_streak_of_habits(iterable)
    returns a tuple containing the habit with the longest streak and the associated streak
list_habits(iterable)
    convinience function that prints out all habits in an iterable
list_checkoffs(habit)
    convinience function that prints out all checkoffs in a habit
'''

import datetime
from typing import Iterable

def get_streaks(habit : "Habit") -> list:
    """get_streaks: returns a list of lists with streaks

    the workflow is
        1. set vars:
            - a copy of the checkoffs list of the give habit (to not change the original => elements will be removed)
            - the "return_list" (list with list of streaks, each streak a list)
        2. set the first "time_period" with the period.Period feature
            a time period is a tuple in the form: (date_start, date_end)
        3. iterate over the checkoffs:
            - check each check_off against the "time_period"
            - if it fits, it is added to the "actual_list" in the return_list and a counter is incremented
                (the ounter is needed to check against the amount of "check_offs" needed to consider a habit unbroken)
                (the "actual_list" refers to the actual unbroken streak)
        4. update the "checkoffs_copy" with only elements that arent added to the "return_list"
        5. check if the streak is broken (a new list has to be added to the ret_lst)
            conditions are:
                1. is the counter equal or greater as the amount checkoffs needed in order to be not broken?
                2. is the "checkoffs_copy" empty? => then the function is done no need to add anything
                3. if the last streak_list is empty 
                    (e.g. a time period is skipped because there are no valid checks against the "time_period"
                        then there is no need to add a new streak_list
        6. increment time_period, and if there are elements left in the checkoffs_copy repeat from 3
    
    Parameter
    ---------
    habit : habit.Habit

    Return
    ------
    list_streaks : list
        list of streaks represented by a list => [[streak1_date1, streak1_date2, ...], [streak2_date1, streak2_date2, ...], [...]]
    """

    def _set_time_period(start: datetime.date) -> tuple:
        """_set_time_period: helper function to set the time period"""
        return habit.periodicity(start, 0), habit.periodicity(start, 1)

    checkoffs_copy = habit.checkoffs.copy()
    list_streaks = [list()]
    time_period = _set_time_period(habit.creation_date)

    def _set_streak_lst() -> None:
        """_set_streak_lst: helper function to break down the complexiety"""
        nonlocal checkoffs_copy
        added_counter = 0

        for check in checkoffs_copy:
            if time_period[0] <= check < time_period[1]:
                list_streaks[-1].append(check)
                added_counter += 1
        
        checkoffs_copy = [check for check in checkoffs_copy if check not in list_streaks[-1]]

        if not (added_counter >= habit.amount_checkoffs) \
            and checkoffs_copy \
            and list_streaks[-1]: list_streaks.append(list())

    while checkoffs_copy:
        _set_streak_lst()
        time_period = _set_time_period(time_period[1])

    return list_streaks

def get_longest_streak(habit: "Habit") -> list:
    """get_longest_streak: returns the longest streak in a habit

    Parameter
    ---------
    habit : Habit
        represents the habit from which the longest streak is desired
    
    Return
    ------
    longest_streak : list
        a list with the checkoffs of the longest streak
    """
    longest_streak = list()
    streaks = get_streaks(habit)
    for streak in streaks:
        if len(streak) > len(longest_streak): longest_streak = streak
    return longest_streak


def get_habits_by_period(container: Iterable, period: "period.Period") -> list:
    """get_habits_by_period: get_habits_by_period: filters habits by their periodicity

    Parameters
    ----------
    container : Iterable
        iterable with the habits to filter as element
    
    Returns
    -------
    habits_with_period : list
        list with the desired habits
    """
    return [habit for habit in container if habit.periodicity.periodicity == period]
    
    # habits_with_period = list()
    # for habit in container:
    #     if habit.periodicity.periodicity == period:
    #         habits_with_period.append(habit)
    # return habits_with_period

def is_broken(habit: "Habit") -> bool:
    """is_broken: returns a bool dependent on if the last time period of the given habit is broken
    if broken True

    Parameters
    ----------
    habit : Habit
        habit whre the information about its brokeness is desired
    
    Returns
    -------
    bool
    """
    time_period = (habit.periodicity(datetime.date.today(), -1), habit.periodicity(datetime.date.today(), 0))
    counter = 0

    for checkoff in habit.checkoffs:
        if time_period[0] <= checkoff <= time_period[1]:
            counter += 1

    if counter >= habit.periodicity.amount_checkoffs:
        return False

    return True

def get_longest_streak_of_habits(container: Iterable) -> tuple:
    """get_longest_streak_of_habits: returns a tuple representing the habit with the 
    longest streak in a list of habits

    Parameters
    ----------
    container : Iterable
        the iterable with the habits
    
    Return
    ------
    tuple
        (habit_with_the_longest_streak, list_with_the_checkoffs_of_the_longest_streak)
    """
    linked_habit = None
    longest_streak = list()

    for habit in container:
        if len(get_longest_streak(habit)) > len(longest_streak):
            longest_streak = get_longest_streak(habit)
            linked_habit = habit
    
    return (linked_habit, longest_streak)

def list_habits(container: Iterable) -> None:
    """list_habits: convinience function that prints out the str representations of the habits
    in a iterable of habits"""
    [print(i) for i in container]    

def list_checkoffs(habit: Iterable) -> None:
    """list_checkoffs: convinience function that prints out the name of a habit and all of the checkoffs"""
    print(habit)
    [print(f"  {i}") for i in sorted(habit.checkoffs)]