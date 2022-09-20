"""
module com_storage:
    subclass of Command representing the CLI-Command storage
    for the habit tracker tool habtrack

===== Imports =====
package-intern:
    src.storage
    cli.command

===== Classes =====
Storage(command.Command):
    accesses the storage functionality

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - import - ========== #
import src.storage, cli.command

# ========== - logic - ========== #

class Storage(cli.command.Command):
    """
    class Storage(command.Command):
        accesses the storage functionality

        routes given further (after the actua command) arguments to 
        sub-commands stored as attributes of the object
        relies heavily on the functionality of the Command class
        each sub-command (method) processes further given arguments
        defines mandatory arguments and processes its functionality

        the habits are all stored in one json file project_root/data/habtrack.json
        all there stored habits are recognised as actual active habits
        everytime a cli call is made this file and its habits are loaded

    ===== Methods =====
    serialize:
        stores a specified habit in a seperate file for export
    """ 
    def serialize(self) -> None:
        """
        Atorage.serialize:
            stores a specified habit in a seperate file for export

            the generated file will be in project_root/data/[Habit_Name].json
            needs the -n argument to identify the habit
        """
        args = self._get_args()
        self._get_missing_out(args, "n")
        hab = self._habits[args["n"]]

        src.storage.serialize(hab)
        self._get_success_out(hab.name, f"successfully stored for export as /data/{hab.name}.json")