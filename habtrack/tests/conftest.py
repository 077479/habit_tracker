# ========== - import - ========== #
from src import habit, storage
from cli import cli_start, cli_data
import datetime, pathlib



# ========== - logic - ========== #
# hab_dir = pathlib.Path(__file__).parents[1] / "habtrack"

# ===== - Fixtures - ===== #
def habit_obj():
    """
    habit_obj:
        provides a habit_obj for testing

        habit_attr:
            name: test_habit
            periodicity: monthly
            description: just here to test the modul
            creation_date = 2000-1-1
            amount: 1
    
    ===== Return =====
    hab : habit.Habit
        the habit for the test scenario
    """

    hab = habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")
    hab.creation_date = datetime.date(2000,1,1)

    return hab

def sample_habs():
    """
    sample_habs:
        returns the sampple data
    """

    return storage.deserialize(demo=True)


# ===== - service - ===== #
def backup_storage():
    """
    backup_storage:
        function to make copys of the storage data in order to preserve
        them from changes during funcitonal tests
    """

    orig_habtrack = pathlib.Path(__file__).parents[1] / "data/habtrack.json"
    test_habtrack = pathlib.Path(__file__).parents[1] / "data/habtrack.json.test"

    orig_sample = pathlib.Path(__file__).parents[1] / "data/sample.json"
    test_sample = pathlib.Path(__file__).parents[1] / "data/sample.json.test"

    copy_file(orig=orig_habtrack, dest=test_habtrack)
    copy_file(orig=orig_sample, dest=test_sample)

def roll_back_storage():
    """
    roll_back_storage:
        function to restore teh stored data after the functional tests
    """

    orig_habtrack = pathlib.Path(__file__).parents[1] / "data/habtrack.json"
    test_habtrack = pathlib.Path(__file__).parents[1] / "data/habtrack.json.test"

    orig_sample = pathlib.Path(__file__).parents[1] / "data/sample.json"
    test_sample = pathlib.Path(__file__).parents[1] / "data/sample.json.test"

    copy_file(orig=test_habtrack, dest=orig_habtrack)
    copy_file(orig=test_sample, dest=orig_sample)

    test_sample.unlink()
    test_habtrack.unlink()

def create_samples():
    """
    create_samples:
        create the sample data to ensure a predefined state for testing
    """

    sample = cli_data.sample
    with open((pathlib.Path(__file__).parents[1] / "data/sample.json"), "w") as file:
            file.write(sample)

def copy_file(orig: pathlib.Path, dest: pathlib.Path):
    """
    copy_file:
        help function that copys one file to another destination
    
    ===== Parameters =====
    orig : pathlib.Path
        the file from where the data has to be copied
    dest : pathlib.Path
        the file that is created to preserve the data    
    """

    if not orig.exists():
        with open(orig, "w") as file:
            file.write(orig_data)

    with open(orig, "r") as file:
        orig_data = file.read()
    
    with open(dest, "w") as file:
        file.write(orig_data)

def clean_habit_storage():
    """
    clean_habit_storage:
        removes done testing entries to be ready for the next test
    """
    if (pathlib.Path(__file__).parents[1] / "data/test_habit.json").exists():
            (pathlib.Path(__file__).parents[1] / "data/test_habit.json").unlink()
    if (pathlib.Path(__file__).parents[1] / "data/habtrack.json").exists():
        hab_lst = storage.deserialize()
        hab_lst_clean = [hab for hab in hab_lst if not hab.name == "test_habit"]
        storage.serialize(hab_lst_clean)