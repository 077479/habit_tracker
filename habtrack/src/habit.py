"""
module habit:
    res modul for the tool habit_tracker (habtrack) that provides the representation of a habit

===== Imports =====
built-in:
    datetime
package-intern:
    src.period

===== Classes =====
Habit:
    represents a Habit

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import datetime, src.period


# ========== - logic - ========== #
class Habit:
    """
    class Habit:
        represents the Habit for the habit_tracker tool (habtrack)

    ===== Attributes =====
    _HABIT : bool
        for (de)serializeation to make sure only Habit objects are processed
    name : str
        representing the name of a habit (e.g. clean room)
    periodicity : period.Period
        periodicity of the habit
    amount : int
        amount of check-offs needed in order to fullfill the requirement of the habit
    description : str
        description of the habit
    creation_date : datetime.date
        represents the creation date of the habit
    checkoffs: list
        stores and represents the check offs (i.e. habit is done e.g. room cleaned)

    ===== Methods =====
    check_off:
        creates a date and adds it to the checkoffs list
    set_periodicity:
        for changes of the periodicity
    __str__:
        str representation of object
    __eq__:
        help method for test purpose
    """

    def __init__(self, name: str, periodicity: str, amount: int = 1, description: str = "") -> "Habit":
        """
        ===== Parameters =====
        name : str
            name of the habit
        periodicity : str
            str representation of the habit
        amount : int (optional)
            amount of check-offs needed in order to fullfill the requirement of the habit
        description : str (optional)
            description of the habit
                
        ===== Returns =====
        habit.Habit
        """

        self._HABIT = True
        self.name = name
        self.periodicity = src.period.Period(periodicity)
        self.amount = amount
        self.description = description
        self.creation_date = datetime.date.today()
        self.checkoffs = list()
    
    def check_off(self) -> None:
        """
        Habit.check_off:
            represents one time doing of the habit
            adds a datetime.date object to the checkoffs list"""

        self.checkoffs.append(datetime.date.today())
    
    def set_periodicity(self, arg_periodicity: str, arg_amount: None = None) -> None:
        """
        Habit.set_periodicity:
            helper function to change periodicity

        ===== Parameters =====
        arg_periodicity : str
            periodicity of the habit
        arg_amount : int (optional)
            amount of check-offs needed in order to fullfill the requirement of the habit
        """

        self.periodicity = src.period.Period(arg_periodicity)
        if arg_amount: self.amount = arg_amount
    
    def __str__(self) -> str:
        """
        Habit.__str__:
            for str representation

        ===== Returns =====
        str f"Habit: {self.name} | {self.creation_date} | {self.periodicity.period} | amount: {self.amount}"
        """

        return f"Habit: {self.name} | {self.creation_date} | {self.periodicity.period} | amount: {self.amount}"

    def __eq__(self, other: "Habit") -> bool:
        """
        Habit.__eq__:
            helper method to test for equality used in testing
            uses a changed form of the built-in "any()"

        ===== Parameters =====
        other : habit.Habit
            other habit to check for equality

        ===== Returns =====
        bool
            indicating equality with a given object
        """
        
        equality_operations = [
            self.name == other.name,
            self.periodicity.period == other.periodicity.period,
            self.amount == other.amount,
            self.description == other.description,            
            self.creation_date == other.creation_date,
            self.checkoffs == other.checkoffs
            ]

        for element in equality_operations:
            if not element:
                return False
        return True