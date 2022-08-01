"""
[optional]
- for management
    - python habit_tracker.py mngt --create -n "name" -p "period" [-d "description"] [-a "amount"]
    - python habit_tracker.py mngt --check_off -n "name"
    - python habit_tracker.py mngt --change_period -n "name" -p "period" [-a amount]
    - python habit_tracker.py mngt --delete_habit -n "name"
- for analyse
    - python habit_tracker.py analyse --get_streaks -n "name"
    - python habit_tracker.py analyse --get_longest_streaks -n "name"
    - python habit_tracker.py analyse --get_habits_by_period -p "period"
    - python habit_tracker.py analyse --is_broken -n "name"
    - python habit_tracker.py analyse --get_longest_streak
    - python habit_tracker.py analyse --list_checkoffs -n "name"
    - python habit_tracker.py list
- for storage
    - python habit_tracker.py storage --serialize [-n "name"] ("all" is default, if "-n" is provided then altered)
    - python habit_tracker.py storage --deserialize [-f "file"] ("all" is default, if "-f" is provided then altered)
"""

# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habtrack, argparse


# ========== - logic - ========== #
class Cli_handler:
    """
    parse the sys.argv[1:2] (to only catch the command given)
    check the first element as "command"
    
    move one level down corresponding to the command given (e.g. method "mngt")
    
    in the downmoved parse the next level again but from sys.argv[2:3] to get the next level
        (e.g. mngt create)
    
    then the "create parser" will actual do the magic

    """
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="the cli interface for the habit tracker tool habtrack",
            usage="python habtrack.py [command] [subcommand] [arguments]"
        )

        parser.add_argument("command")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            exit()
        getattr(self, args.command)()

    def mngt(self):
        print("mngt")
    
    def analyse(self):
        print("analyse")
    
    def storage(self):
        print("storage")


if __name__ == "__main__":
    Cli_handler()