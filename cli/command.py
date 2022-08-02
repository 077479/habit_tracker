# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
import habtrack, argparse

# ========== - logic - ========== #
class Command:
    def __init__(self, demo):
        
        self._demo = demo

        parser = argparse.ArgumentParser(
            usage=f"python habtrack.py [mngt, analyse, storage, list_habits] [sub-command]",
            description=f"the CLI command '{type(self).__name__}' of the habit tracker tool habtrack"
            )
        parser.add_argument(
            "sub_command",
            metavar=f"{type(self).__name__}",
            help=f"{[str(i) for i in dir(self) if not i.startswith('_')]}"
            )
        
        args = parser.parse_args(sys.argv[2:3])

        self._sub_command = args.sub_command
        self._get_habits()
        
        if not hasattr(self, args.sub_command) or getattr(self, args.sub_command)=="":
            self._get_wrong_sub_out()

        getattr(self, args.sub_command)()

    def _get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("-n", metavar="name")
        parser.add_argument("-p", metavar="periodicity", choices=["daily", "weekly", "monthly"])
        parser.add_argument("-d", metavar="description", default="")
        parser.add_argument("-a", metavar="amount", type=int, default=1)
        # parser.add_argument("--demo", action="store_true")

        args = parser.parse_args(sys.argv[3:])
        return vars(args)
    
    def _get_habits(self):
        self._habits = {hab.name: hab for hab in habtrack.storage.deserialize(demo=self._demo)}
    
    def _get_habit_lst(self):
        return [self._habits[i] for i in self._habits]

    def _store(self):
        habtrack.storage.serialize([self._habits[i] for i in self._habits], demo=self._demo)

    def _get_success_out(self, arg_substantiv, arg_verb):
        print(f"DONE, '{arg_substantiv}' is {arg_verb}")

    def _get_missing_out(self, arg_dct, *args):
        for arg in args:
            if not arg_dct[arg]:
                print(f"ERROR!!!\nto perform {self._sub_command} the arguments {args} are needed!\nExiting . . .")
                exit()
    
    def _get_wrong_sub_out(self):
        print(f"\nERROR!!!\n\n{type(self).__name__.upper()} has no {self._sub_command.upper()} use one of the following:\n")
        [print(i) for i in dir(self) if not i.startswith('_')]
        print("\nExiting . . .\n")
        exit()