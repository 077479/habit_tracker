import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import pytest
from habtrack import habit, period

@pytest.fixture
def period_obj():
    """returns a period object for test purposes"""
    return period.Period("monthly")

@pytest.fixture
def habit_obj():
    """habit objec : name:test_habit, periodicity:monthly, desc:just here to test the modul checkoffs:[]"""
    return habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")