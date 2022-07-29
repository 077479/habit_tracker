"""
- for storage
    - python habit_tracker.py storage --serialize habit_source
    - python habit_tracker.py storage --deserialize json_source
- for management
    - python habit_tracker.py mngt --create -n "name" -d "description" -p "periodicity"
    - python habit_tracker.py mngt --check_off -n "name"
    - python habit_tracker.py mngt --change_period -n "name" -p "periodicity"
    - python habit_tracker.py mngt --delete_habit -n "name"
- for analyse
    - python habit_tracker.py analyse --get_streaks -n "name"
    - python habit_tracker.py analyse --get_longest_streaks -n "name"
    - python habit_tracker.py analyse --get_habits_by_period -p "periodicity"
    - python habit_tracker.py analyse --is_broken -n "name"
    - python habit_tracker.py analyse --get_longest_streak_of_all
    - python habit_tracker.py analyse --list_checkoffs -n "name"
    - python habit_tracker.py list
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