"""
module main: convinience module to provide a clean api

===== Imports =====
package-intern:
    habit

===== Functions =====
create_habit: creates a habit and returns it
check_off: checks a given habit off
change_period: changes the period to the given specific periodicity and or amountof check offs needed
delete_habit: removes a habit from context without warning

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habit


# ========== - logic - ========== #
def create_habit(name: str, periodicity: str, description: str = "", amount: int = 1)-> habit.Habit:
    """create_habit: creates a habit and returns it

    ===== Parameters =====
    name : str | name of the habit
    periodicity : str | str representation of the periodicity
    description : str [optional] | description of the habit
    amount : int [optional] | amount checkoffs needed to fullfill the requirement of the habit

    ===== Returns =====
    habit.Habit
    """
 
    return habit.Habit(name=name, periodicity=periodicity, description=description, amount=amount)

def check_off(hab: habit.Habit) -> None:
    """check_off: checks off a specific habit (marks a habit as done one time)

    ===== Parameters =====
    hab : habit.Habit | the habit which was done
    """
    hab.check_off()

def change_period(hab: habit.Habit, periodicity: str, amount: int = 1) -> None:
    """change_period: changes the period of a given habit

    ===== Parameters =====
    hab : habit.Habit | the to change habit
    periodicity : str | str representation of the new periodicity
    amount : int [optional] | represents teh amount of checkoffs needed in order to 
        fullfill the requirement of a the habit
    """
    hab.set_periodicity(periodicity, amount)

def delete_habit(hab: habit.Habit) -> None:
    """delete_habit: removes a given habit from context

    does so without warning!

    ===== Parameters =====
    hab : habit.Habit | the to be gone desired habit
    """
    del hab