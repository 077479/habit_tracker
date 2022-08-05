# ========== - import - ========== #
import pytest, datetime
from habtrack import main
from conftest import habit_obj, sample_habs


# ========== - logic - ========== #
# ===== - create_habit test - ===== #
def test_create_habit_type():
    hab = main.create_habit(name="NEMO_TEST", periodicity="daily")
    assert hab.__module__ == "habtrack.habit"

def test_create_habit_name():
    hab = main.create_habit(name="NEMO_TEST", periodicity="daily")
    assert hab.name == "NEMO_TEST"


# ===== - delete_habit test - ===== #
def test_delete_habit_test(sample_habs):
    habs = sample_habs
    
    assert habs[0].name == "work"
    main.delete_habit(habs[0], habs)
    with pytest.raises(AttributeError):
        assert habs[0] == "work"


# ===== - check_off test - ===== #
def test_check_off_len(habit_obj):
    main.check_off(habit_obj)
    assert len(habit_obj.checkoffs) == 1

def test_check_off_date(habit_obj):
    main.check_off(habit_obj)
    assert habit_obj.checkoffs[0] == datetime.date.today()


# ===== - change_period test - ===== #
def test_change_period_type(habit_obj):
    main.change_period(habit_obj, "daily")
    assert habit_obj.periodicity.__module__ == "habtrack.period"
    
def test_change_period_name(habit_obj):
    main.change_period(habit_obj, "daily")
    assert habit_obj.periodicity.period == "daily"