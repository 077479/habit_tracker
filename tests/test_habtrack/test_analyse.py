"""
heavily relies on storage working! => sample habs laods sample file with storage.deserialize("demo")
can easily be changed(the informaton for the creation of the sample file is complety in the conftest.py)
the approach was choosen to tests analyse and storage in one go (as kind of integration test)
"""
# ========== - import - ========== #
import datetime, pytest
from habtrack import analyse
from tests.conftest import habit_obj
from tests.conftest import sample_habs


# ========== - logic - ========== #


# ===== - get_streaks - # ===== #
def test_get_streaks_smoke(habit_obj):
    analyse.get_longest_streak(habit_obj)

def test_get_streaks_type(habit_obj):
    assert isinstance(analyse.get_streaks(habit_obj), list)

def test_get_streaks_isinstance_element_type(habit_obj):
    assert isinstance(analyse.get_streaks(habit_obj)[0], list)

def test_get_streaks_element_len(sample_habs):
    assert len(analyse.get_streaks(sample_habs[0])[0]) == 4

def test_get_streaks_len(sample_habs):
    # [2,4,3,3,1,1]
    lengths = []
    for i in range(6):
        lengths.append(len(analyse.get_streaks(sample_habs[i])))
    assert lengths == [2,4,3,3,1,1]


# ===== - get_longest_streak - ===== #
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


# ===== - get_habits_by_period - ===== #
def test_get_habits_by_period_len_1(sample_habs):
    assert len(analyse.get_habits_by_period(sample_habs, "weekly")) == 2

def test_get_habits_by_period_len_2(sample_habs):
    assert len(analyse.get_habits_by_period(sample_habs, "monthly")) == 2


# ===== - is_broken - ===== # =====##
def test_is_broke_1(sample_habs):
    for hab in sample_habs:
        assert analyse.is_broken(hab)

@pytest.mark.xfail
def test_is_broke_2(sample_habs):
    sample_habs[0].check_off()
    assert analyse.is_broken(sample_habs[0])


# ===== - get_longest_streak_of_habits - ===== #
def test_get_longest_streak_of_habits_type(sample_habs):
    assert isinstance(analyse.get_longest_streak_of_habits(sample_habs), tuple)

def test_get_longest_streak_of_habits_name(sample_habs):
    assert analyse.get_longest_streak_of_habits(sample_habs)[0].name == "pay_rent"

def test_get_longest_streak_of_habits_len(sample_habs):
    assert len(analyse.get_longest_streak_of_habits(sample_habs)[1]) == 8


# # ===== - list_habits - ===== #
def test_list_habits(sample_habs):
    assert "vacuum_clean" in analyse.list_habits(sample_habs)


# ===== - list_checkoffs - ===== #
def test_list_checkoffs(sample_habs):
    assert isinstance(analyse.list_checkoffs(sample_habs[0]), str)