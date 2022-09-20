"""
module mngt:
    subclass of Command representing the CLI-Command mngt
    (management) for the habit tracker tool habtrack

===== Imports =====
package-intern:
    src.main
    cli.command

===== Classes =====
Mngt(command.Command):
    accesses the mngt functionality

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import src.main, cli.command

# ========== - logic - ========== #
class Mngt(cli.command.Command):
    """
    class Mngt(command.Command):
        accesses the mngt functionality

        routes given further (after the actua command) arguments to 
        sub-commands stored as attributes of the object
        relies heavily on the functionality of the Command class
        each sub-command (method) processes further given arguments
        defines mandatory arguments and processes its functionality

        the habits are all stored in one json file project_root/data/habtrack.json
        all there stored habits are recognised as actual active habits
        everytime a cli call is made this file and its habits are loaded

    ===== Methods =====
    create:
        creates a habit
    check_off:
        checks a habit off (marks it as one time fullfilled for a day)
    change_period:
        changes the periodicity of a habit
    delete_habit:
        deletes a habit without warning
    """
    
    def create(self) -> None:
        """
        Mngt.create:
            creates a habit and adds it to the habtrack.json file

            needs -n, -p as minimal arguments
            further accepts -d, -a as arguments to specify the habit
        """

        args = self._get_args()
        self._get_missing_out(args, "n", "p")

        if self._habits and args["n"] in self._habits.keys():
            print(f"\nERROR!\nHabit: '{args['n']}' already exists\nExiting . . .\n")
            exit()

        hab = src.main.create_habit(name=args["n"], periodicity=args["p"], description=args["d"], amount=args["a"])

        self._habits[args["n"]] = hab

        self._get_success_out(args["n"], "created")
        
        self._store()

    def check_off(self) -> None:
        """
        Mngt.check_off:
            marks a habit as one tme fullfilled for the actual day

            needs the -n argument to identify the habit
        """

        args = self._get_args()
        self._get_missing_out(args, "n")

        src.main.check_off(self._habits[args["n"]])
        
        self._get_success_out(args["n"], "checked off for today")

        self._store()

    def change_period(self) -> None:
        """
        Mngt.change_period:
            changes teh period of a habit

            needs the -n, -p argument to identify the habit/periodicity
        """
        args = self._get_args()
        self._get_missing_out(args, "n", "p")
        src.main.change_period(self._habits[args["n"]], args["p"])
        self._get_success_out(args["n"], f"changed to the new periodicity: {args['p']}")
        self._store()

    def delete_habit(self) -> None:
        """
        Mngt.delete_habit:
            deletes a habit from context and from the file habtrack.json
        """
        args = self._get_args()
        self._get_missing_out(args, "n")

        del self._habits[args["n"]]
        self._get_success_out(args["n"], "deleted")

        self._store()