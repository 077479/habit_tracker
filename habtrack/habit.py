'''
the file habit.py provides the core object(Habit) for the habit_tracker tool (hab_trak)

Imports
-------
pathlib : for import mngt
sys : for import mngt
datetime : for time mngt
period : as representation of the periodicity

Classes
-------
Habit :
    the class that represents a Habit

Exceptions
----------
will raise a TypeError exception if the perioidcity isnt known by the invoked period object
(default periodicities: "daily", "weekly", "monthly")
'''

import pathlib, sys, datetime
sys.path.append(str(pathlib.Path(__file__).parent))
import period

class Habit:
    """
    a class to represent a Habit

    Attributes
    ----------
    _HABIT : bool
        helper constant for serialization purpose
    name : name
        for human identification
    periodicity : period.Period
        represents the periodicity
    description : str, optional
        brief description of the habit
    creation_date : datetime.date
        representation of the date when this object was created
    checkoffs : list
        list with all checkoffs

    Methods
    -------
    check_off()
        adds a check_off to the pool
    __str__()
        for easy representation
    __eq__(Habit)
        helper method for test of serialization
    """

    def __init__(self, name: str, periodicity: str, amount_checkoffs: int = 1, description: str = "") -> "Habit":
        """
        Parameters
        ----------
        name : str
            name for human identification
        periodicity : str
            str representaiton of the periodicity
        amount_checkoffs : int
            represents the needed amounts of check_offs in order to not be broken
        description : str
            brief description of the represented habit
        
        Exceptions
            raises TypeError if the periodicity is not valid for the invoked period.Period object
        """

        self._HABIT = True
        self.name = name
        self.periodicity = period.Period(periodicity, amount_checkoffs)
        self.amount_checkoffs = amount_checkoffs
        self.description = description
        self.creation_date = datetime.date.today()
        self.checkoffs = list()
    
    def check_off(self) -> None:
        """adds today to the checkoffs
        a date can be added as often as needed this is because
        it makes no sence to say you have to do things twice a day
        (e.g. brushing tooth) and not the possibility to check that off
        """

        self.checkoffs.append(datetime.date.today())
    
    def __str__(self) -> str:
        """returns a str representation of itself"""
        return f"Habit: {self.name} | {self.creation_date} | {self.periodicity.periodicity}"

    def __eq__(self, other: "Habit") -> bool:
        """helper method to determine if the (de)serialization process was successfully

        works with an inverted version of the built-in "any"
        
        Parameter
        ---------
        other : Habit
            other habit object to determine equality
        
        Return
        ------
        bool
        """
        
        equality_operations = [
            self.name == other.name,
            self.amount_checkoffs == other.amount_checkoffs,
            self.description == other.description,
            self.periodicity.periodicity == other.periodicity.periodicity,
            self.creation_date == other.creation_date,
            self.checkoffs == other.checkoffs]

        for element in equality_operations:
            if not element:
                return False
        return True