# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
from habtrack import habit
import pytest

# ========== - logic - ========== #
@pytest.fixture
def habit_obj(request):

    def remove_file():
        if (pathlib.Path(__file__).parents[1] / "data/test_habit.json").exists():
            (pathlib.Path(__file__).parents[1] / "data/test_habit.json").unlink()
    request.addfinalizer(remove_file)

    return  habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")