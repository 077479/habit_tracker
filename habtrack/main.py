"""
the file main.py is a helper modul for the habit_tracker tool (hab_track)

Imports
-------
habtrack.habit
habtrack.period
habtrack.storage

Functions
---------
create_habit(name : str, periodicity : str, amount_checkoffs : str)
delete_habit(hab : habit.Habit)
check_off(hab : habit.Habit)
change_period(hab : habit.Habit, periodicity : str, amount : int)
get_list_of_habits(demo : bool)
"""

import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parent))

import habit, period

def create_habit(name: str, periodicity: str, description: str = "", amount_checkoffs: int = 1)-> habit.Habit:
    """create_habit: returns a hbit object with the given values

    Parameters
    ----------
    name : str
        the name of the habit
    periodicity : str
        the periodicity only valid is ["daily", "weekly", "monthly"]
    amount_checkoffs : int, optional
        the amount of checkoffs needed within one time-period in order to not count as broken

    Return
    ------
    habit.Habit    
    """
    return habit.Habit(name=name, periodicity=periodicity, description=description, amount_checkoffs=amount_checkoffs)

def delete_habit(hab: habit.Habit) -> None:
    """delete_habit: deletes the reference to a given habit
    
    Parameter
    ---------
    hab : habit.Habit
    """
    pass

def check_off(hab: habit.Habit) -> None:
    """check_off: calls the check_off method of a habit
    
    Parameter
    ---------
    hab : habit.Habit
    """
    hab.check_off()

def change_period(hab: habit.Habit, periodicity: str, amount: int = 1) -> None:
    """change_period: changes teh period on a given habit

    Parameter
    ---------
    hab : habit.Habit
        the habit where the period is in need of change
    periodicity : str
        the new periodicity
    amount : int
        the amount of checkoffs needed within one time-period in order to not count as broken
    """
    hab.periodicity = period.Period(periodicity, amount_checkoffs=amount)