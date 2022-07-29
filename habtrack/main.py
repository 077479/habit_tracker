import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parent))

import habit, period, storage

def create_habit(name: str, periodicity: str, description: str = "", amount_checkoffs: int = 1)-> habit.Habit:
    return habit.Habit(name=name, periodicity=periodicity, description=description, amount_checkoffs=amount_checkoffs)

def delete_habit(hab: habit.Habit) -> None:
    pass

def check_off(hab: habit.Habit) -> None:
    hab.check_off()

def change_period(hab: habit.Habit, periodicity: str, amount: int = 1) -> None:
    hab.periodicity = period.Period(periodicity, amount_checkoffs=amount)

def get_list_of_stored_habits(demo: bool = False):
    pass
