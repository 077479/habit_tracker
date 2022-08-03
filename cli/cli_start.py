"""
module cli_start: starts the cli for hte habit tool habtrack


===== Imports =====
package-intern
    habtrack
    cli.com_analyse
    cli.com_mngt
    cli.com_storage
    cli.cli_data.sample
    cli.cli_data.man


===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""
# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
import argparse
import habtrack
from cli import com_analyse, com_mngt, com_storage, cli_data


# ========== - logic - ========== #
class CLI_Start:
    """
    class Cli_Handler: entry point of an CLI of the habit tracking tool Habtrack


    ===== Attributes =====
    demo : bool | represents if the CLI will run in "demo mode"


    ===== Methods =====
    mngt
        starts the habit management functionality
    
    analyse
        starts the habit analyse functionality
    
    storage
        starts the habit storage functionality, at the moment only to export single habits
    
    list_habits
        calls a part from the analyse functionality for convinience
    
    demo_default
        resets the sample data for the "demo mode"
    
    man
        shows a bief manual how to use the tool with example
    """
    def __init__(self):
        """
        entrypoint for the CLI

        uses argparse for convinience to get the first command
        calls the first argument that was given
        checks direct for the "demo flag" and removes the argument
        """
        parser = argparse.ArgumentParser(
            description="the cli interface for the habit tracker tool habtrack",
            usage="python habtrack.py [command] [subcommand] [arguments]",
            epilog="for the complete manual use 'python habtrack.py man'"
        )

        parser.add_argument("command", help=f"{[str(i) for i in dir(self) if not i.startswith('_')]}")

        # TODO REFACTORING change this to an argument with defaul val

        self.demo = False
        if "--demo" in sys.argv:
            self.demo = True
            sys.argv.remove("--demo")

        args = parser.parse_args(sys.argv[1:2])
        
        getattr(self, args.command)()

    def mngt(self):
        """
        Command.mngt: just initiates the management functionality object
        """
        com_mngt.Mngt(self.demo)

    def analyse(self):
        """
        Command.analyse: just initiates the analyse functionality object
        """
        com_analyse.Analyse(self.demo)
    
    def storage(self):
        """
        Command.storage: just initiates the storage functionality object
        """
        com_storage.Storage(self.demo)
    
    def list_habits(self):
        """
        Command.list_habits: just lists all stored habits (either sample if demo is given or regular)
        """
        if self.demo:
            habs = habtrack.storage.deserialize(file_source="sample")
        else:
            habs = habtrack.storage.deserialize()
        print(habtrack.analyse.list_habits(habs))
    
    def demo_default(self):
        """
        Command.demo_default: creates/resets the sammple data
        """
        with open((pathlib.Path(__file__).parent / "data/sample.json"), "w") as file:
                file.write(cli_data.sample)
    
    def man(self):
        """
        Command.man: shows the manual of the tool
        """
        print(cli_data.man)