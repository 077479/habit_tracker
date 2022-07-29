# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import datetime


# ========== - logic - ========== #
class Period:

    def __init__(self, period: str) -> "Period":
    
        self.periods = {"daily":self._add_day, "weekly":self._add_week, "monthly":self._add_month}
        self.period = period
        self._set_fct(period)
    
    def _set_fct(self, period: str) -> None:

        if not period in self.periods:
            raise TypeError(f"{period} is not a valid option as periodicity")
        self.fct = self.periods[period]
    
    def _add_day(self, start_date: datetime.date, increment: int) -> tuple:
        start = start_date
        end = datetime.date.fromordinal(start_date.toordinal() + increment)

        if increment < 0:
            return (end, start)

        return (start, end)

    def _add_week(self, start_date: datetime.date, increment: int) -> None:
        start = start_date
        end = datetime.date.fromordinal(start_date.toordinal() + increment*7)

        if increment < 0:
            return (end, start)

        return (start, end)

    def _add_month(self, start_date: datetime.date, increment: int) -> None:

        all_months = start_date.year * 12 + start_date.month - 1 + increment
        year = all_months // 12
        month = all_months % 12 + 1

        start = start_date
        end = datetime.date(year, month, start_date.day)

        if increment < 0:
            return (end, start)

        return (start, end)

    def __call__(self, start_date: datetime.date, increment: int) -> None:

        return self.fct(start_date, increment)