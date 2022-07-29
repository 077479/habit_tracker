# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habit


# ========== - logic - ========== #
def create_habit(name: str, periodicity: str, description: str = "", amount: int = 1)-> habit.Habit:
 
     return habit.Habit(name=name, periodicity=periodicity, description=description, amount=amount)

def check_off(hab: habit.Habit) -> None:
    hab.check_off()

def change_period(hab: habit.Habit, periodicity: str, amount: int = 1) -> None:
    hab.set_periodicity(periodicity, amount)

def delete_habit(hab: habit.Habit) -> None:
    del hab