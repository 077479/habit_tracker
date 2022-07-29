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

"""get_streaks: method that returns a list of list of streaks

Parameter
---------
habit : Habit
the habit where the streaks has to be listed

Return
------
list
representing the streaks as list of lists of checkoffsc e.g. 
[[str_1_check_1, str_1_check_2]], [str_2_check_1, str_2_check_2]]
"""
"""_set_time_period: helper method that returns a list of list of streaks

Parameter
---------
start : datetime.date
    the date from where the time period has to be created

Return
------
tuple(datetime.date, datetime.date)
    representing the time period (from set_time_period[0] to set_time_period[1])
"""
"""_lst_diff: helper method that aims to mimic the difference functionality from a set

Parameter
---------
lst_1 : list
    the list where the elements has to be removed
lst_2 : list
    the list where the elements to remove are provided
"""
"""_set_streak_list: the actual magic happens here

1. it iterates over the list of checkoffs in a habit
2. it checks every element if its within the provided time period
3. if it is, it is added to the streak_list in the return_list and
    a counter is incremented
4. the counter is checked against the amount of checkoffs needed in order to
    mark the time_period as not broken
5. if this check is fails, a new streak_list is added to the return_list
6. after that the elements added to teh return_list are removed from the list with checkoffs

after that it is again called with an incremented time_period

Parameter
---------
checkoffs : list
    list with checkoffs
time_period : tuple
    represents the time period => (datetime.date_1, datetime.date_2)
ret_lst : list
    represents the list with the list of streaks

"""
import datetime
from typing import Iterable

def get_streaks(habit : "Habit") -> list:
    
    def _set_time_period(start : datetime.date) -> tuple:
        return (period(start, 0), period(start, 1))

    def _set_streak_list() -> None:

        added = False
        counter = 0
        for check in checkoffs:
            if time_period[0] <= check <= time_period[1]:

                counter += 1
                streaks_lst[-1].append(check)
        
        [checkoffs.remove(item) for item in streaks_lst[-1] if item in checkoffs]

        if counter >= amount_checkoffs: added=True
        if not added and streaks_lst[-1]: streaks_lst.append(list())



    checkoffs = habit.checkoffs.copy()
    period = habit.periodicity
    creation_date = habit.creation_date
    streaks_lst = [list()]
    time_period = _set_time_period(creation_date)
    amount_checkoffs = period.amount_checkoffs

    while checkoffs:
        _set_streak_list()
        time_period = _set_time_period(time_period[1])

    return streaks_lst

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


def get_habits_by_period(container: Iterable, period: "Period") -> list:
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