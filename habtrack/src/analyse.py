"""
module analyse:
    analyse modul of the habit_tracker tool (habtrack)
    provides functionality to get insight into habits or list of habits

===== Imports =====
built-in:
    datetime, typing.Iterable

===== Functions =====
get_streaks:
    returns a list of lists where each list is representing a streak
    e.g. [[streak_1_date1, streak_1_date2, ...], [streak_2_date1, streak_2_date2, ...], [streak_3_date1, streak_3_date2, ...]]
get_longest_streak:
    returns the streak_list with the most elements, representing the longest streak of a habit
get_habits_by_period:
    returns a list of habits with the same period of a given list of habits
is_broken:
    checks if a habit was fullfilled in his last time-period
get_longest_streak_of_habits:
    get the longest streak out of a list of habits
list_habits:
    returns a formatted str with the names of all habits in a list of habits
list_checkoffs:
    returns a formatted str with the name of the habit and all checkoffs

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import datetime
from typing import Iterable


# ========== - logic - ========== #
def get_streaks(hab : object) -> list:
    """
    get_streaks:
        returns a list of lists with streaks

    the workflow is
        1. set vars:
            - a copy of the checkoffs list of the given habit (to not change the original => elements will be removed)
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
    hab : habit.Habit

    Return
    ------
    list_streaks : list
        list of streaks represented by a list => [[streak1_date1, streak1_date2, ...], [streak2_date1, streak2_date2, ...], [...]]
    """

    checkoffs_copy = hab.checkoffs.copy()
    streaks = [list()]
    time_period = hab.periodicity(hab.creation_date, 1)

    def _set_streak_lst() -> None:
        """_set_streak_lst: helper function to break down the complexiety"""
        nonlocal checkoffs_copy
        added_counter = 0

        for check in checkoffs_copy:
            if time_period[0] <= check < time_period[1]:
                streaks[-1].append(check)
                added_counter += 1
        
        checkoffs_copy = [check for check in checkoffs_copy if check not in streaks[-1]]

        if not (added_counter >= hab.amount) \
            and checkoffs_copy \
            and streaks[-1]: streaks.append(list())

    while checkoffs_copy:
        _set_streak_lst()
        time_period = hab.periodicity(time_period[1], 1)

    return streaks

def get_longest_streak(hab: object) -> list:
    """
    get_longest_streak:
        gets the longest streak of a habti
        goes through the streaks and takes the longest one

    ===== Parameters =====
    hab: habit.Habit

    ===== Returns =====
    longest_streak : list
        list with the dates of the checkoffs representing the longest streak
    """

    longest_streak = list()
    streaks = get_streaks(hab)
    for streak in streaks:
        if len(streak) > len(longest_streak): longest_streak = streak
    return longest_streak

def get_habits_by_period(hab_container: Iterable, period: str) -> list:
    """
    get_habits_by_period:
        searches for habits with the same periodicity within a list of habti obj

    ===== Parameters =====
    hab_container : list
        the habit list
    period : str
        the desired periodicity
            
    ===== Returns =====
    list
        with the habits with the desired periodicity
    """

    return [hab for hab in hab_container if hab.periodicity.period == period]

def is_broken(hab: object) -> bool:
    """
    is_broken:
        checks if the last time-period of the given habit was fullfilled

        just creates the last time period and checks the check offs against it
        RETURNS TRUE IF THE HHABIT WAS NOT FULLFILLED

    ===== Parameters =====
    hab : habit.Habit

    ===== Returns =====
    bool
        representing if the habit was fullfilled or not
    """

    time_period = (hab.periodicity(datetime.date.today(), -1))
    counter = 0

    for checkoff in hab.checkoffs:
        if time_period[0] <= checkoff <= time_period[1]:
            counter += 1

    if counter >= hab.amount:
        return False

    return True

def get_longest_streak_of_habits(hab_container: Iterable) -> tuple:
    """
    get_longest_streak_of_habits:
        checks for the habit wit hte longest streak in
        a list of habits

    ===== Parameters =====
    hab_container : list
            
    ===== Returns =====
    tuple | (linked_habit : habit.Habit, longest_streak : list)
    """

    linked_habit = None
    longest_streak = list()

    for hab in hab_container:
        if len(get_longest_streak(hab)) > len(longest_streak):
            longest_streak = get_longest_streak(hab)
            linked_habit = hab
    
    return (linked_habit, longest_streak)

def list_habits(hab_container: Iterable) -> str:
    """
    list_habits:
        returns a str representing all habits in a list of habits

    ===== Parameters =====
    hab_container : list    
        
    ===== Returns =====
    ret_str : str
        the formatted string with the names of the habits
    """

    ret_str = "stored habits:"
    for hab in hab_container:
        ret_str += f"\n    {hab}"
    return ret_str


def list_checkoffs(hab: object) -> str:
    """
    list_checkoffs:
        returns a str with the name and checkoffs

    ===== Parameters =====
    hab : habit.Habit
        the habit with the desired information
            
    ===== Returns =====
    ret_str : str
        the formatted string with the name and the checkoffs of the habit
    """
    
    ret_str = f"{hab}"
    for check in hab.checkoffs:
        ret_str += f"\n   {check}"
    
    return ret_str
