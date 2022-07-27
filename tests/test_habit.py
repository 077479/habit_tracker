import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import pytest, datetime
from habtrack import habit

############### - TODO outsource to conftest.py - ###############
@pytest.fixture
def habit_obj():
    return habit.Habit("test_habit", "monthly", "just here to test the modul")



############### - init test - ###############
def test_habit_init_name(habit_obj):
    assert habit_obj.name == "test_habit"
def test_habit_init_desc(habit_obj):
    assert habit_obj.description == "just here to test the modul"
def test_habit_init_periodicity(habit_obj):
    assert habit_obj.periodicity(datetime.date(2000,1,1), 1) == datetime.date(2000,2,1)

@pytest.mark.parametrize("periods", [None, "gibberish", 13])
def test_habit_defect_parameters(periods):
    with pytest.raises(TypeError):
        habit.Habit(periods)

############### - check_off test - ###############
def test_habit_check_off_created(habit_obj):
    habit_obj.check_off()
    assert habit_obj.checkoffs[0] == datetime.date.today()

def test_habit_check_off_amount(habit_obj):
    for i in range(5):
        habit_obj.check_off()
    assert len(habit_obj.checkoffs) == 5



############### - __str__ test - ###############
def test_habit_str_repr(habit_obj):
    assert str(habit_obj) == f"Habit: test_habit | {str(datetime.date.today())} | monthly"



############### - __eq__ test - ###############
def test_habit_equality_true(habit_obj):
    assert habit_obj == habit.Habit("test_habit", "monthly", "just here to test the modul")

@pytest.mark.xfail
@pytest.mark.parametrize("defect", [habit.Habit("test", "monthly"), 235, "nice", habit.Habit("john", "weekly")])
def test_habit_equality_defect(habit_obj, defect):
    assert habit_obj == defect