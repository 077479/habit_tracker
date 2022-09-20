"""
Package habtrack

    tool to keep track of habits

    the __init__ of the project root is utilized to provide clean api calls to the functionality
    therefor methods of objects are imported as listed below

    usage: "habtrack [command] [subcommand]"

    for a reference how to use try:
        habtrack reference

    for a brief semi interactive introduction try:
        habtrack man

===== Imports =====
built_in
    pathlib, sys

package_intern
    src.storage.serialize
    src.storage.deserialize

    src.main.create_habit
    src.main.check_off
    src.main.change_period
    src.main.delete_habit

    src.analyse.get_streaks
    src.analyse.get_longest_streak
    src.analyse.is_broken
    src.analyse.get_habits_by_period
    src.analyse.get_longest_streak_of_habits

    src.analyse.list_habits
    src.analyse.list_checkoffs

===== Subpackages =====
src
    actual implementation of the logic
cli
    cli package
tests
    provides the test suit

===== Modules =====
habtrack
    cli entry point

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5"
"""

import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))

from src.storage import serialize
from src.storage import deserialize

from src.main import create_habit
from src.main import check_off
from src.main import change_period
from src.main import delete_habit

from src.analyse import get_streaks
from src.analyse import get_longest_streak
from src.analyse import is_broken
from src.analyse import get_habits_by_period
from src.analyse import get_longest_streak_of_habits

from src.analyse import list_habits
from src.analyse import list_checkoffs