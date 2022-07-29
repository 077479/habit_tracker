'''
the file period.py is a helper modul for the habit_tracker tool (hab_trak)
that represents the periodicity of a habit

Imports
-------
the class periodicity depends on "datetime"

Classes
-------
Period :
    the class that represents the periodicity

Exceptions
----------
will raise a TypeError exception if the perioidcity isnt known by the class
(default periodicities: "daily", "weekly", "monthly")
'''

import datetime

class Period:
    """
    a class to represent periodicities

    the then created object will have the functionality to return the end of a
    time-span

    to determine this functionality dynamically the method to do so is linked
    to a string in a dict

    Attributes
    ----------
    periods: dict
        the dictionary that maps the time-span creating methods to a string
    periodicity : str
        the string given to set the time-span creating method
    amount_checkoffs : int, optional
        the number of checkoffs that have to achieved within a time-span
    fct : function call
        the actual time-span generating method

    Methods
    -------
    _set_fct(periodicity)
        links the method to generate the time-period to the attribute 'fct'
    _add_day(start_date, increment)
        the method that generates a timespan from one day to another
    _add_week(start_date, increment)
        the method that generates a timespan from one week to another
    _add_month(start_date, increment)
        the method that generates a time-span from one month to another
    """

    def __init__(self, periodicity: str, amount_checkoffs: int =1) -> "Period":
        """
        Parameters
        ----------
        periodicity : str
            the string given to set the time-span creating method
        amount_checkoffs : int
            the number of checkoffs that have to achieved within a time-span
        """
        self.periods = {"daily":self._add_day, "weekly":self._add_week, "monthly":self._add_month}
        self.periodicity = periodicity
        self.amount_checkoffs = amount_checkoffs
        self._set_fct(periodicity)
    
    def _set_fct(self, periodicity: str) -> None:
        """Sets the time-span generating method

        Parameters
        ----------
        periodicity : str
            the string given to set the time-span creating method
        
        Exceptions
            if periodicity is not in the object attribute periods a TypeError
            is raised
        """
        if not periodicity in self.periods:
            raise TypeError(f"{periodicity} is not a valid option as periodicity")
        self.fct = self.periods[periodicity]
    
    def _add_day(self, start_date: datetime.date, increment: int) -> None:
        """Returns the end of a time period

        Parameters
        ----------
        start_date : datetime.date
            the starting date from where to create the time-span
        increment : int
            the amount of days to go forward to get the end of the time-span
        
        Returns
        -------
        datetime.date marking the end of the timespan
        """
        return datetime.date.fromordinal(start_date.toordinal() + increment)

    def _add_week(self, start_date: datetime.date, increment: int) -> None:
        """Returns the end of a time period

        Parameters
        ----------
        start_date : datetime.date
            the starting date from where to create the time-span
        increment : int
            the amount of weeks to go forward to get the end of the time-span
        
        Returns
        -------
        datetime.date marking the end of the timespan
        """
        return datetime.date.fromordinal(start_date.toordinal() + increment*7)

    def _add_month(self, start_date: datetime.date, increment: int) -> None:
        """Returns the end of a time period

        Parameters
        ----------
        start_date : datetime.date
            the starting date from where to create the time-span
        increment : int
            the amount of month to go forward to get the end of the time-span
        
        Returns
        -------
        datetime.date marking the end of the timespan
        """
        all_months = start_date.year * 12 + start_date.month - 1 + increment
        # print(all_months)
        year = all_months // 12
        month = all_months % 12 + 1
        return datetime.date(year, month, start_date.day)

    def __call__(self, start_date: datetime.date, increment: int) -> None:
        """calls the actual functionality (return the end of a timespan)

        Parameters
        ----------
        start_date : datetime.date
            the starting date from where to create the time-span
        increment : int
            the amount of incremnts to go forward to get the end of the time-span
        
        Returns
        -------
        datetime.date representing the end of the timespan
        """
        return self.fct(start_date, increment)