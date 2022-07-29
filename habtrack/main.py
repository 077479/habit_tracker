# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habit


# ========== - logic - ========== #
def create_habit(name: str, period: str, description: str = "", amount: int = 1)-> habit.Habit:
 
     return habit.Habit(name=name, period=period, description=description, amount=amount)

def check_off(hab: habit.Habit) -> None:
    hab.check_off()

def change_period(hab: habit.Habit, period: str, amount: int = 1) -> None:
    hab.periodicity = (period, amount)

def delete_habit(hab: habit.Habit) -> None:
    del hab