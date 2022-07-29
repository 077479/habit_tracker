# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import period
import datetime


# ========== - logic - ========== #
class Habit:

    def __init__(self, name: str, period: str, amount: int = 1, description: str = "") -> "Habit":

        self._HABIT = True
        self.name = name
        self.period = period.Period(period)
        self.amount = amount
        self.description = description
        self.creation_date = datetime.date.today()
        self.checkoffs = list()
    
    def check_off(self) -> None:

        self.checkoffs.append(datetime.date.today())
    
    @property
    def period(self):
        return self.period
    @period.setter
    def period(self, *args):

        period_new, amount_new = args

        self.periodicity = period.Period(period_new)
        self.amount = amount_new

    
    def __str__(self) -> str:

        return f"Habit: {self.name} | {self.creation_date} | {self.period.period} | amount: {self.amount}"

    def __eq__(self, other: "Habit") -> bool:
        
        equality_operations = [
            self.name == other.name,
            self.amount == other.amount,
            self.description == other.description,
            self.period.period == other.period.period,
            self.creation_date == other.creation_date,
            self.checkoffs == other.checkoffs]

        for element in equality_operations:
            if not element:
                return False
        return True