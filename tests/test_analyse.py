import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]))

from habtrack import analyse
from tests.conftest import habit_obj

########## - get_streaks test - ####################
########## - get_longest_streak test - #############
########## - get_habits_by_period test- ############
########## - is_broken test - ######################
########## - get_longest_streak_of_habits test - ###
########## - list_habits test - ####################
########## - list_checkoffs test - #################