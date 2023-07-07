"""
module period:
    ressource module for the tool habit_tracker (habtrack)

===== Imports =====
buit-in:
    datetime

===== Classes =====
Period:
    represents a periodicity for a habit object

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5

===== Exceptions =====
TypeError:
    when initializing the period object, and a wrong str repr of the periodicity is given
"""
# ========== - import - ========== #
import datetime


# ========== - logic - ========== #
class Period:
    """
    class Period:
            represents the periodicity for a habit in a habitat_tracker tool

    ===== Attributes =====
    _periods : dict
        mapping of the str representation of a periodicity to an actual functionality to 
        return a time-period
    period : str
        the str representation of the periodicity
    fct : function
        the linking of the functionality from the periods dict

    ===== Methods =====
    _set_fct:
        maps the fct to the functionality
    _add_day:
        functionality that returns a daily timeperiod
    _add_week:
        functionality that returns a weekly timeperiod
    add_month:
        functionality that returns a monthly timeperiod
    __call__:
        calls the fct
    """

    def __init__(self, period: str) -> "Period":
        """
        ===== Parameters =====
        period : str
            the str representation of the string

        ===== Returns =====
        Period Object

        ===== Exceptions =====
        TypeError:
            when initializing the period object, when the str representation of
            the periodicity is not part of the periods dict
        """
    
        self._periods = {"daily":self._add_day, "weekly":self._add_week, "monthly":self._add_month}
        self.period = period
        self._set_fct(period)
    
    def _set_fct(self, period: str) -> None:
        """
        Period._set_fct:
            maps the fct to the functionality

        ===== Parameters =====
        period : str
            the str representation of the string
                
        ===== Exceptions =====
        TypeError:
            when initializing the period object, when the str representation of
            the periodicity is not part of the periods dict
        """

        if not period in self._periods:
            raise TypeError(f"{period} is not a valid option as periodicity")
        self.fct = self._periods[period]
    
    def _add_day(self, start_date: datetime.date, increment: int) -> tuple:
        """
        Period._add_day:
            provides the time-period generation functionality

            translates the given date into ordinal, adds the val from increment
            REVERSES the returnvalues if a negative increment is given (end, start)

        ===== Parameters =====
        start_date : datetime.date
            represents the start_date of the time period
        icrement : int
            represents the time span between the start/end date
                
        ===== Returns =====
        tuple
            (start, end) => if increment<0 (end, start)
        """

        start = start_date
        end = datetime.date.fromordinal(start_date.toordinal() + increment)

        if increment < 0:
            return (end, start)

        return (start, end)

    def _add_week(self, start_date: datetime.date, increment: int) -> None:
        """
        Period._add_week:   
            provides the time-period generation functionality

            translates the given date into ordinal, adds the val from increment times 7
            REVERSES the returnvalues if a negative increment is given (end, start)

        ===== Parameters =====
        start_date : datetime.date
            represents the start_date of the time period
        icrement : int
            represents the time span between the start/end date
                
        ===== Returns =====
        tuple
            (start, end) => if increment<0 (end, start)
        """

        start = start_date
        end = datetime.date.fromordinal(start_date.toordinal() + increment*7)

        if increment < 0:
            return (end, start)

        return (start, end)

    def _add_month(self, start_date: datetime.date, increment: int) -> None:
        """
        Period._add_month:
            provides the time-period generation functionality

            translates the given date into the amount of months adds the increment
            retranslates the amount of moths to years/months just hands the day of the month
            over
            
            !a -1 is needed in order for the calculation, else the "val%12" gives trouble)

            REVERSES the return values if a negative increment is given (end, start)

        ===== Parameters =====
        start_date : datetime.date
            represents the start_date of the time period
        icrement : int
            represents the time span between the start/end date
                
        ===== Returns =====
        tuple
            (start, end) => if increment<0 (end, start)
        """

        all_months = start_date.year * 12 + start_date.month - 1 + increment
        year = all_months // 12
        month = all_months % 12 + 1

        start = start_date
        end = datetime.date(year, month, start_date.day)

        if increment < 0:
            return (end, start)

        return (start, end)

    def __call__(self, start_date: datetime.date, increment: int) -> None:
        """
        Period.__call__:
            calls the time-period functionality

        ===== Parameters =====
        start_date : datetime.date
            represents the start_date of the time period
        icrement : int
            represents the time span between the start/end date    
        
        ===== Returns =====
        functioncall fct
        """

        return self.fct(start_date, increment)