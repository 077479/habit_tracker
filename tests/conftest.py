import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))

# ========== - import - ========== #
from habtrack import habit, storage
from unittest.mock import create_autospec
import pytest, datetime, pathlib

# ========== - logic - ========== #
@pytest.fixture
def habit_obj(request):
    """depends on storage working!"""
    def remove_file():
        if (pathlib.Path(__file__).parents[1] / "data/test_habit.json").exists():
            (pathlib.Path(__file__).parents[1] / "data/test_habit.json").unlink()
        if (pathlib.Path(__file__).parents[1] / "data/habtrack.json").exists():
            hab_lst = storage.deserialize()
            hab_lst_clean = [hab for hab in hab_lst if not hab.name == "test_habit"]
            storage.serialize(hab_lst_clean)
    request.addfinalizer(remove_file)

    hab = habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")
    hab.creation_date = datetime.date(2000,1,1)

    return hab

@pytest.fixture
def create_samples():
    with open((pathlib.Path(__file__).parents[1] / "data/tests.json"), "w") as file:
            file.write("""[
    {
        "_HABIT":true,
        "name":"work",
        "description":"daily[1], Streaks[2] 4/4",
        "periodicity":"daily",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730121,
            730122,
            730123,
            730125,
            730126,
            730127,
            730128
        ]
    },
    {
        "_HABIT":true,
        "name":"eat",
        "description":"daily[2], Streaks[4] 2/4/1/1",
        "periodicity":"daily",
        "amount":2,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730120,
            730122,
            730122,
            730123,
            730123,
            730125,
            730126
        ]
    },
    {
        "_HABIT":true,
        "name":"swimming",
        "description":"weekly[1], Streaks[3] 2/2/4",
        "periodicity":"weekly",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730123,
            730129,
            730141,
            730146,
            730161,
            730165,
            730167,
            730172
        ]
    },
    { 
        "_HABIT":true,
        "name":"vacuum_clean",
        "description":"weekly[3], Streaks[3] 5/2/1",
        "periodicity":"weekly",
        "amount":3,
        "creation_date":730120,
        "checkoffs": [
            730122,
            730124,
            730126,
            730128,
            730131,
            730142,
            730146,
            730156
        ]
    },
    {
        "_HABIT":true,
        "name":"pay_rent",
        "description":"monthly[1], Streaks[1] 8",
        "periodicity":"monthly",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730151,
            730180,
            730211,
            730241,
            730272,
            730302,
            730333
        ]
    },
    {
        "_HABIT":true,
        "name":"shop",
        "description":"monthly[4], Streaks[1] 8",
        "periodicity":"monthly",
        "amount":4,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730128,
            730135,
            730148,
            730150,
            730156,
            730163,
            730172
        ]
    }
]""")

@pytest.fixture
def sample_habs(create_samples, request):
    """depends on storage working!"""
    
    def remove_samples():
        if (pathlib.Path(__file__).parents[1] / "data/tests.json").exists():
            (pathlib.Path(__file__).parents[1] / "data/tests.json").unlink()
    request.addfinalizer(remove_samples)

    create_samples
    return storage.deserialize(file_source="tests")
