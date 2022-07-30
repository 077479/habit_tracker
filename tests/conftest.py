# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
from habtrack import habit, storage
import pytest, datetime, json

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
def sample_habs():
    """depends on storage working!"""
    return storage.deserialize(demo=True)