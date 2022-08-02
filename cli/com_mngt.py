# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
import habtrack
from cli import command

# ========== - logic - ========== #

class Mngt(command.Command):
    
    def create(self):

        args = self._get_args()
        self._get_missing_out(args, "n", "p")

        if self._habits and args["n"] in self._habits.keys():
            print(f"\nERROR!\nHabit: '{args['n']}' already exists\nExiting . . .\n")
            exit()

        hab = habtrack.main.create_habit(name=args["n"], periodicity=args["p"], description=args["d"], amount=args["a"])

        self._habits[args["n"]] = hab

        self._get_success_out(args["n"], "created")
        
        self._store()

    def check_off(self):
        args = self._get_args()
        self._get_missing_out(args, "n")

        habtrack.main.check_off(self._habits[args["n"]])
        
        self._get_success_out(args["n"], "checked off for today")

        self._store()

    def change_period(self):
        args = self._get_args()
        self._get_missing_out(args, "n", "p")
        habtrack.main.change_period(self._habits[args["n"]], args["p"])
        self._get_success_out(args["n"], f"changed to the new periodicity: {args['p']}")
        self._store()

    def delete_habit(self):
        args = self._get_args()
        self._get_missing_out(args, "n")

        del self._habits[args["n"]]
        self._get_success_out(args["n"], "deleted")

        self._store()