import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import datetime, pytest
from habtrack import analyse
from tests.conftest import habit_obj
from tests.conftest import sample_habs

########## - get_streaks test - ####################
def test_get_streaks_instance(habit_obj):
    assert isinstance(analyse.get_streaks(habit_obj), list)

def test_get_streaks_isinstance_element(habit_obj):
    assert isinstance(analyse.get_streaks(habit_obj)[0], list)

def test_get_streaks_len_element(sample_habs):
    assert len(analyse.get_streaks(sample_habs[0])[0]) == 4

def test_get_streaks_len(sample_habs):
    # [2,4,3,3,1,1]
    lengths = []
    for i in range(6):
        lengths.append(len(analyse.get_streaks(sample_habs[i])))
    assert lengths == [2,4,3,3,1,1]



########## - get_longest_streak test - #############
def test_get_longest_streak_1(sample_habs):
    assert analyse.get_longest_streak(sample_habs[0]) == [
        datetime.date.fromordinal(730120),
        datetime.date.fromordinal(730121),
        datetime.date.fromordinal(730122),
        datetime.date.fromordinal(730123),
    ]

def test_get_longest_streak_2(sample_habs):
    assert analyse.get_longest_streak(sample_habs[3]) == [
        datetime.date.fromordinal(730122),
        datetime.date.fromordinal(730124),
        datetime.date.fromordinal(730126),
        datetime.date.fromordinal(730128),
        datetime.date.fromordinal(730131)
    ]



########## - get_habits_by_period test- ############
def test_get_habits_by_period_len_1(sample_habs):
    assert len(analyse.get_habits_by_period(sample_habs, "weekly")) == 2

def test_get_habits_by_period_len_2(sample_habs):
    assert len(analyse.get_habits_by_period(sample_habs, "monthly")) == 2



########## - is_broken test - ######################
def test_is_broke_1(sample_habs):
    for hab in sample_habs:
        assert analyse.is_broken(hab)



########## - get_longest_streak_of_habits test - ###
def test_get_longest_streak_of_habits_type(sample_habs):
    assert isinstance(analyse.get_longest_streak_of_habits(sample_habs), tuple)

def test_get_longest_streak_of_habits_name(sample_habs):
    assert analyse.get_longest_streak_of_habits(sample_habs)[0].name == "pay_rent"

def test_get_longest_streak_of_habits_len(sample_habs):
    assert len(analyse.get_longest_streak_of_habits(sample_habs)[1]) == 8



########## - list_habits test - ####################
@pytest.mark.skip
def test_list_habits(sample_habs):
    assert analyse.list_habits(sample_habs) == None


@pytest.mark.skip
########## - list_checkoffs test - #################
def test_list_checkoffs(sample_habs):
    assert analyse.list_checkoffs(sample_habs[0]) == None