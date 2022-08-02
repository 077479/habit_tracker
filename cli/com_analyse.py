# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
import habtrack
from cli import command
# ========== - logic - ========== #

class Analyse(command.Command):
    def get_streaks(self):
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        hab_streaks = habtrack.analyse.get_streaks(hab)

        print(f"\n{hab} | Streaks:")
        [print(i) for i in hab_streaks]
        print()


    def get_longest_streak(self):
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        hab_streak = habtrack.analyse.get_longest_streak(hab)

        print(f"\n{hab} | Longest Streak:")
        print(hab_streak)
        print()

    def get_habits_by_period(self):        
        args = self._get_args()
        self._get_missing_out(args, "p")

        habs = habtrack.analyse.get_habits_by_period(self._get_habit_lst(), args["p"])
        print(habtrack.analyse.list_habits(habs))

    def is_broken(self):        
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        result = habtrack.analyse.is_broken(hab)
        answer = "unbroken"

        if result: answer = "broken"
        print(f"the Habit: '{hab.name}' is currently: {answer}")

    def get_longest_streak_of_habits(self):
        hab, streak = habtrack.analyse.get_longest_streak_of_habits(self._get_habit_lst())
        print(f"\nthe habit of the stored habits with the longest streak is:\n{hab}")
        print(f"Streak:\n{streak}\n")


    def list_checkoffs(self):
        """
        - python habit_tracker.py list
        """
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        print(habtrack.analyse.list_checkoffs(hab))

    def list_habits(self):
        print(habtrack.list_habits([self._habits[i] for i in self._habits]))