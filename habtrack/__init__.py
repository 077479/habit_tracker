"""
Package

===== linked API Calls =====

===== Classes =====

===== Functions =====

===== Imports =====

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5

===== Exceptions =====
"""


import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parent))

import storage
import analyse
import main
import habit
import period

from storage import serialize
from storage import deserialize

from main import create_habit
from main import check_off
from main import change_period
from main import delete_habit

from analyse import get_streaks
from analyse import get_longest_streak
from analyse import is_broken
from analyse import get_habits_by_period
from analyse import get_longest_streak_of_habits

from analyse import list_habits
from analyse import list_checkoffs