"""
module cli_start
    starts the cli for the habit tool habtrack

===== Imports =====
built-ins
    argparse, sys, pathlib

package-intern
    src.storage
    src.analyse

    cli.com_analyse
    cli.com_mngt
    cli.com_storage
    cli.cli_data.sample
    cli.cli_data.man

===== Classes =====
CliStart
    entry point class for the cli
"""
# ========== - import - ========== #
import argparse, sys, pathlib
import src.storage, src.analyse
import cli.com_analyse, cli.com_mngt, cli.com_storage, cli.cli_data, cli.manual


# ========== - logic - ========== #
class CliStart:
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

    def __init__(self) -> None:
        """
        entrypoint for the CLI

        uses argparse for convinience to get the first command
        calls the first argument that was given
        checks direct for the "demo flag" and removes the argument
        """

        # ========== - Parser - ========== #
        parser = argparse.ArgumentParser(
            description="the cli interface for the habit tracker tool habtrack",
            usage="python habtrack.py [command] [subcommand] [arguments]",
            epilog="for the complete manual use 'python habtrack.py man'"
        )
        parser.add_argument("command", help=f"{[str(i) for i in dir(self) if not i.startswith('_')]}")
        parser.error = self.parser_error

        # ========== - demo flag - ========== #
        self.demo = False
        if "--demo" in sys.argv:
            self.demo = True
            sys.argv.remove("--demo")

        # ========== - functionality - ========== #
        args = parser.parse_args(sys.argv[1:2])        
        if not hasattr(self, args.command): self.parser_error()

        getattr(self, args.command)()

    def test_first_time(self) -> None:
        """get the first time user message out"""
        with open(pathlib.Path(__file__).parents[1] / "data/habtrack.json", "r") as file:
            hab_js = file.readlines()
        if len(hab_js) < 5 and not self.demo:
            e_len = 5
            e_mes = f"{'='*e_len} - no data detected - {'='*e_len}"
            print(f"\n{e_mes}")
            print("there seems to be no data stored, is this your first time using this tool?\nif so you should run 'python habtrack.py man' for a brief manual")
            print(f"{e_mes}\n")

    def parser_error(self, *args) -> None:
        e_len = 5
        e_mes = f"{'='*e_len} - help - {'='*e_len}"
        print(f"\n{e_mes}")
        print("Try as subcommand:")
        print(cli.cli_data.info_command)
        print("  or try 'python habtrack.py man' for a short semi-interactive manual")
        print(f"{e_mes}\n")
        exit(1)
    
    def help(self) -> None:
        self.parser_error()

    def mngt(self) -> None:
        """
        Command.mngt: just initiates the management functionality object
        """
        self.test_first_time()
        cli.com_mngt.Mngt(self.demo)

    def analyse(self) -> None:
        """
        Command.analyse: just initiates the analyse functionality object
        """
        self.test_first_time()
        cli.com_analyse.Analyse(self.demo)
    
    def storage(self) -> None:
        """
        Command.storage: just initiates the storage functionality object
        """
        self.test_first_time()
        cli.com_storage.Storage(self.demo)
    
    def list_habits(self) -> None:
        """
        Command.list_habits: just lists all stored habits (either sample if demo is given or regular)
        """
        if self.demo:
            habs = src.storage.deserialize(file_source="sample")
        else:
            habs = src.storage.deserialize()
        print(src.analyse.list_habits(habs))
    
    def demo_default(self) -> None:
        """
        Command.demo_default: creates/resets the sammple data
        """
        with open((pathlib.Path(__file__).parents[1] / "data/sample.json"), "w") as file:
                file.write(cli.cli_data.sample)
        print("\nDone, demo data is reseted to origin\n")

    def reference(self) -> None:
        print(cli.cli_data.reference)
    
    def man(self) -> None:
        """
        Command.man: shows the manual of the tool
        """
        cli.manual.run()