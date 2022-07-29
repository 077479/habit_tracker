# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import datetime
from typing import Iterable


# ========== - logic - ========== #
def get_streaks(hab : "habit.Habit") -> list:
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
        time_period = hab.periodicity(time_period[1])

    return streaks

def get_longest_streak(hab: "habit.Habit") -> list:

    longest_streak = list()
    streaks = get_streaks(hab)
    for streak in streaks:
        if len(streak) > len(longest_streak): longest_streak = streak
    return longest_streak

def get_habits_by_period(hab_container: Iterable, period: str) -> list:

    return [hab for hab in hab_container if hab.periodicity.period == period]

def is_broken(hab: "habit.Habit") -> bool:

    time_period = (hab.periodicity(datetime.date.today(), -1))
    counter = 0

    for checkoff in hab.checkoffs:
        if time_period[0] <= checkoff <= time_period[1]:
            counter += 1

    if counter >= hab.amount:
        return False

    return True

def get_longest_streak_of_habits(hab_container: Iterable) -> tuple:

    linked_habit = None
    longest_streak = list()

    for hab in hab_container:
        if len(get_longest_streak(hab)) > len(longest_streak):
            longest_streak = get_longest_streak(hab)
            linked_habit = hab
    
    return (linked_habit, longest_streak)

def list_habits(hab_container: Iterable) -> str:

    ret_str = "stored habits:"
    for hab in hab_container:
        ret_str += f"\n {hab.name}"
    return ret_str


def list_checkoffs(hab: Iterable) -> str:
    
    ret_str = f"{hab.name}"
    for check in hab.checkoffs:
        ret_str += f"\n  {check}"
    
    return ret_str
