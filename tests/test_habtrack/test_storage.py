# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))


# ========== - import - ========== #
import datetime, pathlib, pytest
from habtrack import storage
from tests.conftest import sample_habs


# ========== - logic - ========== #

# ===== - _serialize_habit test - ===== #
def test__serialize_habit_type(habit_obj):
    assert isinstance(storage._serialize_habit(habit_obj), dict)

def test__serialize_habit_dct_name(habit_obj):
    assert storage._serialize_habit(habit_obj)["name"] == "test_habit"

def test__serialize_habit_dct_period(habit_obj):
    assert storage._serialize_habit(habit_obj)["periodicity"] == "monthly"

def test__serialize_habit_dct_desc(habit_obj):
    assert storage._serialize_habit(habit_obj)["description"] == "just here to test the modul"

def test__serialize_habit_dct_creation_date(habit_obj):
    assert storage._serialize_habit(habit_obj)["creation_date"] == datetime.date(2000,1,1).toordinal()

def test__serialize_habit_dct_checkoffs(habit_obj):
    habit_obj.checkoffs.append(datetime.date.fromordinal(730120)) # 2000,1,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730151)) # 2000,2,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730180)) # 2000,3,1
    habit_obj.checkoffs.append(datetime.date.fromordinal(730211)) # 2000,4,1
    assert storage._serialize_habit(habit_obj)["checkoffs"] == [730120, 730151, 730180, 730211]



# ===== - serialize test - ===== #
def test_serialize_single_file_creation(habit_obj):
    storage.serialize(habit_obj)
    assert (pathlib.Path(__file__).parents[2] / "data/test_habit.json").exists()


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
def test_serialize_single_file_content(habit_obj, result):
    storage.serialize(habit_obj)
    with open (pathlib.Path(__file__).parents[2] / "data/test_habit.json", "r") as file:
        for line in file.readline():
            line == result

def test_serialize_collection_file_creation(habit_obj):
    storage.serialize([habit_obj])
    assert (pathlib.Path(__file__).parents[2] / "data/habtrack.json").exists()

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
def test_serialize_collection_file_content(habit_obj, result):
    storage.serialize([habit_obj])
    with open (pathlib.Path(__file__).parents[2] / "data/habtrack.json", "r") as file:
        for line in file.readline():
            line == result


# ===== - _deserialize test - ===== #
def test__deserialize(habit_obj):
    hab = storage._deserialize_habit({
        "_HABIT": True,
        "name": "test_habit",
        "description": "just here to test the modul",
        "periodicity": "monthly",
        "amount": 1,
        "creation_date": 730120,
        "checkoffs": []
        })
    assert hab == habit_obj


# ===== - deserialize test - ===== #
def test_deserialize_smoke():
    storage.deserialize()

def test_deserialize_type():
    assert isinstance(storage.deserialize(), list)

def test_deserialize_demo_type(sample_habs):
    sample_habs
    assert storage.deserialize(file_source="tests")[0].__module__ == "habit"

def test_deserialize_demo_len(sample_habs):
    sample_habs
    assert len(storage.deserialize(file_source="tests")) == 6

def test_deserialize_file_source_len(habit_obj):
    storage.serialize([habit_obj])
    assert len(storage.deserialize(file_source="habit_obj")) == 1

def test_deserialize_file_source_name(habit_obj):
    storage.serialize([habit_obj])
    assert storage.deserialize(file_source="habit_obj")[0].name == "test_habit"