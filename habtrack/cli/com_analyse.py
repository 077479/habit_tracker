"""
module com_analyse:
    subclass of Command representing the CLI-Command analyse
    for the habit tracker tool habtrack

===== Imports =====
package-intern:
    src.analyse
    cli.command

===== Classes =====
Analyse(command.Command): 
    accesses the analyse functionality

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import cli.command
from src import analyse


# ========== - logic - ========== #

class Analyse(cli.command.Command):
    """
    class Analyse(command.Command): 
        accesses the analyse functionality

        routes given further arguments to sub-commands stored as attributes of the object
        relies heavily on the functionality of the Command class
        each sub-command (method) processes further given arguments
        defines mandatory arguments and processes its functionality

        the habits are all stored in one json file project_root/data/habtrack.json
        all there stored habits are recognised as actual active habits
        everytime a cli call is made this file and its habits are loaded

    ===== Methods =====
    get_streaks:
        shows the streaks of a habit on the terminal
    get_longest_streak:
        shows the longest streak of a habit
    get_habits_by_period:
        shows habits with the same period
    is_broken:
        shows if a requirement of a given habit was fullfilled in the last time-period
    get_longest_streak_of_habits:
        returnes the habit with the longest streak
    list_checkoffs:
        shows all checkoffs of a habit
    list_habits:
        lists all habits stored in the default location
    """
    def get_streaks(self) -> None:
        """
        Analyse.get_streak:
            shows the streaks of a habit

            needs the -n argument to identify the habit
        """

        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        #! hab_streaks = src.analyse.get_streaks(hab)
        hab_streaks = analyse.get_streaks(hab)

        print(f"\n{hab} | Streaks:")
        [print(i) for i in hab_streaks]
        print()


    def get_longest_streak(self) -> None:
        """
        Analyse.get_longest_streak:
            shows the longest streaks of a habit

            needs the -n argument to identify the habit
        """
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        #! hab_streak = src.analyse.get_longest_streak(hab)
        hab_streak = analyse.get_longest_streak(hab)

        print(f"\n{hab} | Longest Streak:")
        print(hab_streak)
        print()

    def get_habits_by_period(self) -> None:  
        """
        Analyse.get_habits_by_period:
            shows only habits with a certain periodicity

            needs the -p argument to define the periodicity
        """      
        args = self._get_args()
        self._get_missing_out(args, "p")

        #! habs = src.analyse.get_habits_by_period(self._get_habit_lst(), args["p"])
        #! print(src.analyse.list_habits(habs))
        habs = analyse.get_habits_by_period(self._get_habit_lst(), args["p"])
        print(analyse.list_habits(habs))

    def is_broken(self) -> None:
        """
        Analyse.is_brocen:
            shows if a habit is was fullfilled the last time-period

            needs the -n argument to identify the habit
        """  
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        #! result = src.analyse.is_broken(hab)
        result = analyse.is_broken(hab)
        answer = "unbroken"

        if result: answer = "broken"
        print(f"the Habit: '{hab.name}' is currently: {answer}")

    def get_longest_streak_of_habits(self) -> None:
        """
        Analyse.get_longest_streak_of_habits:
            shows the longest streaks of all stored habits
        """
        #! hab, streak = src.analyse.get_longest_streak_of_habits(self._get_habit_lst())
        hab, streak = analyse.get_longest_streak_of_habits(self._get_habit_lst())
        print(f"\nthe habit of the stored habits with the longest streak is:\n{hab}")
        print(f"Streak:\n{streak}\n")


    def list_checkoffs(self) -> None:
        """
        Analyse.list_checkoffs:
            lists all checkoffs of a given habit
        
            needs the -n argument to determine the habit
        """
        args = self._get_args()
        self._get_missing_out(args, "n")

        hab = self._habits[args["n"]]
        #! print(src.analyse.list_checkoffs(hab))
        print(analyse.list_checkoffs(hab))


    def list_habits(self) -> None:
        """
        Analyse.list_habits:
            lists all stored habits
        """
        #! print(src.analyse.list_habits([self._habits[i] for i in self._habits]))
        print(analyse.list_habits([self._habits[i] for i in self._habits]))