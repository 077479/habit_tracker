"""
[optional]
- for management
    - python habit_tracker.py mngt --create -n "name" -p "period" [-d "description"] [-a "amount"]
    - python habit_tracker.py mngt --check_off -n "name"
    - python habit_tracker.py mngt --change_period -n "name" -p "period" [-a amount]
    - python habit_tracker.py mngt --delete_habit -n "name"
- for analyse
    - python habit_tracker.py analyse --get_streaks -n "name"
    - python habit_tracker.py analyse --get_longest_streak -n "name"
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
class Mngt:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("sub_command")
        args = parser.parse_args(sys.argv[2:3])
        
        self.habits = {hab.name: hab for hab in habtrack.storage.deserialize()}
        
        getattr(self, args.sub_command)()        

    def create(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", metavar="name", required=True)
        parser.add_argument("-p", metavar="periodicity", required=True, choices=["daily", "weekly", "monthly"])
        parser.add_argument("-d", metavar="description", default="")
        parser.add_argument("-a", metavar="amount", type=int, default=1)

        arg_dct = vars(parser.parse_args(sys.argv[3:]))
        self.habits[arg_dct["n"]] = habtrack.main.create_habit(name=arg_dct["n"], periodicity=arg_dct["p"], description=arg_dct["d"], amount=arg_dct["a"])
        
        habtrack.storage.serialize([self.habits[i] for i in self.habits])

    def check_off(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", metavar="name", required=True)
        arg_dct = vars(parser.parse_args(sys.argv[3:]))

        habtrack.main.check_off(self.habits[arg_dct["n"]])

        habtrack.storage.serialize([self.habits[i] for i in self.habits])

    def change_period(self):
        habtrack.main.change_period()

    def delete_habit(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", metavar="name", required=True)
        arg_dct = vars(parser.parse_args(sys.argv[3:]))

        lst = [self.habits[i] for i in self.habits]

        habtrack.main.delete_habit(self.habits[arg_dct["n"]], lst)

        habtrack.storage.serialize(lst)

class Analyse:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("sub_command")
        args = parser.parse_args(sys.argv[2:3])
        
        self.habits = {hab.name: hab for hab in habtrack.storage.deserialize()}

        getattr(self, args.sub_command)()
    
    def get_streaks(self):
        habtrack.analyse.get_streaks()
    def get_longest_streaks(self):
        habtrack.analyse.get_longest_streak()
    def get_habits_by_period(self):
        habtrack.analyse.get_habits_by_period()
    def is_broken(self):
        habtrack.analyse.is_broken()
    def get_longest_streak(self):
        habtrack.analyse.get_longest_streak()
    def list_checkoffs(self):
        habtrack.analyse.list_checkoffs()
    def list_habits(self):
        print(habtrack.list_habits([self.habits[i] for i in self.habits]))

class Storage:
    def serialize(self):
        habtrack.storage.serialize()
    def deserialize(self):
        habtrack.storage.deserialize()







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
            print(f"{sys.argv[0]} is not a valid command, use 'mngt', 'analyse' or 'storage'")
            exit()
        getattr(self, args.command)()

    def mngt(self):
        Mngt()

    def analyse(self):
        Analyse()
    
    def storage(self):
        Storage()
    
    def create_sample(self):
        with open(pathlib.Path(__file__).parent / "data/sample.json", "w") as file:
            file.write("""[
    {
        "_HABIT":true,
        "name":"work",
        "description":"daily[1], Streaks[2] 4/4",
        "periodicity":"daily",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730121,
            730122,
            730123,
            730125,
            730126,
            730127,
            730128
        ]
    },
    {
        "_HABIT":true,
        "name":"eat",
        "description":"daily[2], Streaks[4] 2/4/1/1",
        "periodicity":"daily",
        "amount":2,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730120,
            730122,
            730122,
            730123,
            730123,
            730125,
            730126
        ]
    },
    {
        "_HABIT":true,
        "name":"swimming",
        "description":"weekly[1], Streaks[3] 2/2/4",
        "periodicity":"weekly",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730123,
            730129,
            730141,
            730146,
            730161,
            730165,
            730167,
            730172
        ]
    },
    { 
        "_HABIT":true,
        "name":"vacuum_clean",
        "description":"weekly[3], Streaks[3] 5/2/1",
        "periodicity":"weekly",
        "amount":3,
        "creation_date":730120,
        "checkoffs": [
            730122,
            730124,
            730126,
            730128,
            730131,
            730142,
            730146,
            730156
        ]
    },
    {
        "_HABIT":true,
        "name":"pay_rent",
        "description":"monthly[1], Streaks[1] 8",
        "periodicity":"monthly",
        "amount":1,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730151,
            730180,
            730211,
            730241,
            730272,
            730302,
            730333
        ]
    },
    {
        "_HABIT":true,
        "name":"shop",
        "description":"monthly[4], Streaks[1] 8",
        "periodicity":"monthly",
        "amount":4,
        "creation_date":730120,
        "checkoffs": [
            730120,
            730128,
            730135,
            730148,
            730150,
            730156,
            730163,
            730172
        ]
    }
]""")

if __name__ == "__main__":
    Cli_handler()