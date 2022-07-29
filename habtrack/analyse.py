import datetime
from typing import Iterable

def get_streaks(hab : "Habit") -> list:
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

    def _set_time_period(start: datetime.date) -> tuple:
        """_set_time_period: helper function to set the time period"""
        return hab.periodicity(start, 0), hab.periodicity(start, 1)

    checkoffs_copy = hab.checkoffs.copy()
    list_streaks = [list()]
    time_period = _set_time_period(hab.creation_date)

    def _set_streak_lst() -> None:
        """_set_streak_lst: helper function to break down the complexiety"""
        nonlocal checkoffs_copy
        added_counter = 0

        for check in checkoffs_copy:
            if time_period[0] <= check < time_period[1]:
                list_streaks[-1].append(check)
                added_counter += 1
        
        checkoffs_copy = [check for check in checkoffs_copy if check not in list_streaks[-1]]

        if not (added_counter >= hab.amount_checkoffs) \
            and checkoffs_copy \
            and list_streaks[-1]: list_streaks.append(list())

    while checkoffs_copy:
        _set_streak_lst()
        time_period = _set_time_period(time_period[1])

    return list_streaks

def get_longest_streak(hab: "Habit") -> list:

    longest_streak = list()
    streaks = get_streaks(hab)
    for streak in streaks:
        if len(streak) > len(longest_streak): longest_streak = streak
    return longest_streak

def get_habits_by_period(container: Iterable, period: "period.Period") -> list:

    return [hab for hab in container if hab.periodicity.periodicity == period]

def is_broken(hab: "Habit") -> bool:

    time_period = (hab.periodicity(datetime.date.today(), -1), hab.periodicity(datetime.date.today(), 0))
    counter = 0

    for checkoff in hab.checkoffs:
        if time_period[0] <= checkoff <= time_period[1]:
            counter += 1

    if counter >= hab.periodicity.amount_checkoffs:
        return False

    return True

def get_longest_streak_of_habits(container: Iterable) -> tuple:

    linked_habit = None
    longest_streak = list()

    for habit in container:
        if len(get_longest_streak(habit)) > len(longest_streak):
            longest_streak = get_longest_streak(habit)
            linked_habit = habit
    
    return (linked_habit, longest_streak)

def list_habits(container: Iterable) -> None:

    ret_str = "stored habits:"
    for hab in container:
        ret_str += f"\n {hab.name}"
    return ret_str


def list_checkoffs(hab: Iterable) -> None:
    
    ret_str = f"{hab.name}"
    for check in hab.checkoffs:
        ret_str += f"\n  {check}"
    
    return ret_str
