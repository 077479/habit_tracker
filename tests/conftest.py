import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import pytest, pathlib, json, datetime
from habtrack import habit, period, storage, analyse


@pytest.fixture
def period_obj():
    """returns a period object for test purposes"""
    return period.Period("monthly")

@pytest.fixture
def habit_obj():
    """habit objec : name:test_habit, periodicity:monthly, desc:just here to test the modul checkoffs:[]"""
    return habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")

@pytest.fixture
def sample_habs():
    """sample_habs: returns a list with the sample habits from "project_root"/data/sample.json"""
    sample_path = pathlib.Path(__file__).parents[1] / "data/sample.json"
    sample_habs = list()

    with open(sample_path, "r") as file:
        for hab in json.load(file):
            sample_habs.append(storage._deserialize_habit(hab))
    
    return sample_habs