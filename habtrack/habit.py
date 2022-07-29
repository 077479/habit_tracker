# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import period
import datetime


# ========== - logic - ========== #
class Habit:

    def __init__(self, name: str, periodicity: str, amount: int = 1, description: str = "") -> "Habit":

        self._HABIT = True
        self.name = name
        self.periodicity = period.Period(periodicity)
        self.amount = amount
        self.description = description
        self.creation_date = datetime.date.today()
        self.checkoffs = list()
    
    def check_off(self) -> None:

        self.checkoffs.append(datetime.date.today())
    
    def set_periodicity(self, arg_periodicity: str, arg_amount: None = None) -> None:
        self.periodicity = period.Period(arg_periodicity)
        if arg_amount: self.amount = arg_amount
    
    def __str__(self) -> str:

        return f"Habit: {self.name} | {self.creation_date} | {self.periodicity.period} | amount: {self.amount}"

    def __eq__(self, other: "Habit") -> bool:
        
        equality_operations = [
            self.name == other.name,
            self.amount == other.amount,
            self.description == other.description,
            self.periodicity.period == other.periodicity.period,
            self.creation_date == other.creation_date,
            self.checkoffs == other.checkoffs]

        for element in equality_operations:
            if not element:
                return False
        return True