from distutils.util import change_root
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import pytest, datetime
from habtrack import main, habit
from conftest import habit_obj, sample_habs

########## - create_habit test - ##########
def test_create_habit_type():
    hab = main.create_habit(name="NEMO_TEST", periodicity="daily")
    assert hab.__module__ == "habit"

def test_create_habit_name():
    hab = main.create_habit(name="NEMO_TEST", periodicity="daily")
    assert hab.name == "NEMO_TEST"



########## - delete_habit test - ##########
@pytest.mark.skip
def test_delete_habit_test():
    hab = habit.Habit(name="test", periodicity="weekly")
    main.delete_habit(hab)
    with pytest.raises(UnboundLocalError):
        assert hab.name == "test"



########## - check_off test - ##########
def test_check_off_len(habit_obj):
    main.check_off(habit_obj)
    assert len(habit_obj.checkoffs) == 1

def test_check_off_date(habit_obj):
    main.check_off(habit_obj)
    assert habit_obj.checkoffs[0] == datetime.date.today()



########## - change_period test - ##########
def test_change_period_type(habit_obj):
    main.change_period(habit_obj, "daily")
    assert habit_obj.periodicity.__module__ == "period"
    

def test_change_period_name(habit_obj):
    main.change_period(habit_obj, "daily")
    assert habit_obj.periodicity.periodicity == "daily"



########## - get_list_of_stored_habits test - ##########
@pytest.mark.skip
def test_get_list():
    assert main.get_list_of_stored_habits(demo = True) == [hab.names for hab in sample_habs]