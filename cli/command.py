"""
module command: provides the interface for the command implementations

===== Imports =====
built-in:
    argparse
    sys
package-intern:
    habtrack

===== Classes =====
Command:
    provides the interface for the command implementations

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import argparse, sys
import habtrack


# ========== - logic - ========== #
class Command:
    """
    class Command:  
        this class provides shared functionality for the actual command implmentations

    ===== Attributes =====
    _demo : bool
        determines if the tool runs in "demo-mode"
    _sub_command : function_call
        the subcommand that is called for
    _habits : dict
        the list of habits stored in the data directory
        with the name of the habit as key and the value as habtrack.habit.Habit
        !means there cant be duplicate names

    ===== Methods =====
    _get_args:
        parses the arguments for the subcommands
    _get_habits:
        loads the habit from the file either habtrack.json or sample.json
    _get_habit_lst:
        returns a list of habits (the api works mostly with lists)
    _store:
        stores the habits into file
    _get_success_out:
        respponse after a call is done (ui responsiveness)
    _get_missing_out:
        checks for mandatory arguments (e.g. -n for name of a habit)
    _get_wrong_sub_out:
        response after a wrong sub_command is called (ui responsiveness)
    """

    def __init__(self, demo: bool) -> None:
        """
        parses the next argument given and checks it against the attributes for the correct subcommand
        """
        self._demo = demo

        parser = argparse.ArgumentParser(
            usage=f"python habtrack.py [mngt, analyse, storage, list_habits] [sub-command]",
            description=f"the CLI command '{type(self).__name__}' of the habit tracker tool habtrack"
            )
        parser.add_argument(
            "sub_command",
            metavar=f"{type(self).__name__}",
            help=f"wrong command: {[str(i) for i in dir(self) if not i.startswith('_')]}"
            )
        
        args = parser.parse_args(sys.argv[2:3])

        self._sub_command = args.sub_command
        self._get_habits()
        
        if not hasattr(self, args.sub_command) or getattr(self, args.sub_command)=="":
            self._get_wrong_sub_out()

        getattr(self, args.sub_command)()

    def _get_args(self) -> dict:
        """
        Command._get_args:
            helper that parses the left arguments
            (after the subcommand is done)

        ===== Returns =====
        vars(args) : dict
            the dictionary containing the arguments 
            TODO REFACTORING the vars call is not neccessary
        """

        parser = argparse.ArgumentParser()

        parser.add_argument("-n", metavar="name")
        parser.add_argument("-p", metavar="periodicity", choices=["daily", "weekly", "monthly"])
        parser.add_argument("-d", metavar="description", default="")
        parser.add_argument("-a", metavar="amount", type=int, default=1)
        # parser.add_argument("--demo", action="store_true")

        args = parser.parse_args(sys.argv[3:])
        return vars(args)
    
    def _get_habits(self) -> None:
        """
        Command._get_habits:
            helper method that loads the habits from file
        """
        self._habits = {hab.name: hab for hab in habtrack.storage.deserialize(demo=self._demo)}
    
    def _get_habit_lst(self) -> list:
        """
        Command._get_habit_lst:
            returns a list of the stored habits
            (most of the api processes lists)
        """
        return [self._habits[i] for i in self._habits]

    def _store(self) -> None:
        """
        Command._store:
            helper method to save the habits to file
        """
        habtrack.storage.serialize([self._habits[i] for i in self._habits.keys()], demo=self._demo)

    def _get_success_out(self, arg_substantiv, arg_verb) -> None:
        """
        Command._get_success_out:
            helper method to standardize the ui response
        """
        print(f"DONE, '{arg_substantiv}' is {arg_verb}")

    def _get_missing_out(self, arg_dct, *args) -> None:
        """
        Command._get_missing_out:
            helper method to check for the correct arguments
            to standardize the ui response
        """
        for arg in args:
            if not arg_dct[arg]:
                print(f"ERROR!!!\nto perform {self._sub_command} the arguments {args} are needed!\nExiting . . .")
                exit()
    
    def _get_wrong_sub_out(self) -> None:
        """
        Command._get_wrong_sub_out:
            helper method to respond to a wrong sub-command given
        """
        print(f"\nERROR!!!\n\n{type(self).__name__.upper()} has no {self._sub_command.upper()} use one of the following:\n")
        [print(i) for i in dir(self) if not i.startswith('_')]
        print("\nExiting . . .\n")
        exit()