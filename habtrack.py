# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habtrack, argparse, cli


# ========== - logic - ========== #
# ===== Entry Point ===== #
class Cli_handler:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="the cli interface for the habit tracker tool habtrack",
            usage="python habtrack.py [command] [subcommand] [arguments]"
        )

        parser.add_argument("command", help=f"{[str(i) for i in dir(self) if not i.startswith('_')]}")

        self.demo = False
        if "--demo" in sys.argv:
            self.demo = True
            sys.argv.remove("--demo")

        args = parser.parse_args(sys.argv[1:2])
        
        getattr(self, args.command)()

    def mngt(self):
        cli.com_mngt.Mngt(self.demo)

    def analyse(self):
        cli.com_analyse.Analyse(self.demo)
    
    def storage(self):
        import cli
        cli.com_storage.Storage(self.demo)
    
    def list_habits(self):
        if self.demo:
            habs = habtrack.storage.deserialize(file_source="sample")
        else:
            habs = habtrack.storage.deserialize()
        print(habtrack.analyse.list_habits(habs))
    
    def demo_default(self):
        with open((pathlib.Path(__file__).parent / "data/sample.json"), "w") as file:
                file.write(cli.cli_data.sample)
    
    def man(self):
        print(cli.cli_data.man)


if __name__ == "__main__":
    Cli_handler()