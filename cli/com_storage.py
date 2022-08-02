# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))


# ========== - import - ========== #
import habtrack
from cli import command

# ========== - logic - ========== #

class Storage(command.Command):
    def serialize(self):
        args = self._get_args()
        self._get_missing_out(args, "n")
        hab = self._habits[args["n"]]

        habtrack.storage.serialize(hab)
        self._get_success_out(hab.name, f"successfully stored for export as /data/{hab.name}.json")