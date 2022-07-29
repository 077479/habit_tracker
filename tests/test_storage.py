import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import datetime, pathlib, pytest
from habtrack import storage
from tests.conftest import habit_obj

########## - _serialize_habit test - ##########
# habit objec : name:test_habit, periodicity:monthly, desc:just here to test the modul checkoffs:[]

def test__serialize_habit_type(habit_obj):
    assert isinstance(storage._serialize_habit(habit_obj), dict)

def test__serialize_habit_dct_name(habit_obj):
    assert storage._serialize_habit(habit_obj)["name"] == "test_habit"

def test__serialize_habit_dct_period(habit_obj):
    assert storage._serialize_habit(habit_obj)["periodicity"] == "monthly"

def test__serialize_habit_dct_desc(habit_obj):
    assert storage._serialize_habit(habit_obj)["description"] == "just here to test the modul"

def test__serialize_habit_dct_creation_date(habit_obj):
    assert storage._serialize_habit(habit_obj)["creation_date"] == datetime.date.today().toordinal()

def test__serialize_habit_dct_checkoffs(habit_obj):
    habit_obj.checkoffs.append(datetime.date.fromordinal(730120)) # 2000,1,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730151)) # 2000,2,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730180)) # 2000,3,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730211)) # 2000,4,1
    assert storage._serialize_habit(habit_obj)["checkoffs"] == [730120, 730151, 730180, 730211]



########## - serialize_habit test - ##########
def test_serialize_habit_single_file_creation(habit_obj):
    # habit objec : name:test_habit, periodicity:monthly, desc:just here to test the modul checkoffs:[]
    storage.serialize_habit(habit_obj)
    assert (pathlib.Path(__file__).parents[1] / "data/test_habit.json").exists()

@pytest.mark.parametrize("result", [
    '{',
    '  "_HABIT": true',
    '  "name": "test_habit"',
    '  "description": "just here to test the modul"',
    '  "periodicity": "monthly"',
    '  "amount_checkoffs": 1',
    '  "creation_date": 738364',
    '  "checkoffs": []',
    '}'
])
def test_serialize_habit_single_file_content(habit_obj, result):
    storage.serialize_habit(habit_obj)
    with open (pathlib.Path(__file__).parents[1] / "data/test_habit.json", "r") as file:
        for line in file.readline():
            line == result

def test_serialize_habit_collection_file_creation(habit_obj):
    storage.serialize_habit([habit_obj])
    assert (pathlib.Path(__file__).parents[1] / "data/habtrack.json").exists()

@pytest.mark.parametrize("result", [
    '[',
    '  {',
    '    "_HABIT": true',
    '    "name": "test_habit"',
    '    "description": "just here to test the modul"',
    '    "periodicity": "monthly"',
    '    "amount_checkoffs": 1',
    '    "creation_date": 738364',
    '    "checkoffs": []',
    '  }',
    ']'
])
def test_serialize_habit_collection_file_content(habit_obj, result):
    storage.serialize_habit(habit_obj)
    with open (pathlib.Path(__file__).parents[1] / "data/habtrack.json", "r") as file:
        for line in file.readline():
            line == result