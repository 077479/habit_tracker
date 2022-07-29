import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

import pytest
from habtrack import analyse
from tests.conftest import habit_obj
from tests.conftest import sample_habs

########## - get_streaks test - ####################
@pytest.mark.parametrize("result", [4, 2, 4, 5, 8, 8])
def test_get_streaks_len(sample_habs, result):
    for hab in sample_habs:
        assert len(analyse.get_streaks(hab)[0]) == result

########## - get_longest_streak test - #############
########## - get_habits_by_period test- ############
########## - is_broken test - ######################
########## - get_longest_streak_of_habits test - ###
########## - list_habits test - ####################
########## - list_checkoffs test - #################