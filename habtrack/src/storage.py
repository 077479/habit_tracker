"""
module storage:
    tool to (de)serialize habit objects from/to files

===== Imports =====
built-in:
    json, datetime, pathlib
package-intern:
    src.habit

===== Globals =====
data_dir : pathlib.Path
    represents the data directory of the tool (root_proj/data)

===== Functions =====
_serialize_habit:
    creates a dictionary from a habit obj
serialize:
    stores a habit or list of habits to a json file
_deserialize:
    creates a habit obj from a dict
deserialize:
    loads json files representing habits into the system

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5

===== Excetions =====
TypeError   
    if a given dict that has to be translated into a Habit is not valid
"""

# ========== - import - ========== #
import src.habit
import json, datetime, pathlib


# ========== - logic - ========== #
data_dir = pathlib.Path(__file__).parents[1] / "data"

# ===== Serialization ===== #
def _serialize_habit(hab: src.habit.Habit) -> dict:
    """
    storage._serialize_habit:
        helper that creates a dictionary from a habit obj

    ===== Parameters =====
    hab : habit.Habit
        the habit that will be transformed to dict

    ===== Returns =====
    dict
        dictionary representation of a given habit
    """

    return {
        "_HABIT": True,
        "name": hab.name,
        "description": hab.description,
        "periodicity": hab.periodicity.period,
        "amount": hab.amount,
        "creation_date": hab.creation_date.toordinal(),
        "checkoffs": [check.toordinal() for check in hab.checkoffs]
    }

def serialize(hab_element: src.habit.Habit | list, demo: bool = False) -> None:
    """
    storage.serialize:
        saves a habit or list of habits to a json file

        creates a json fle with the name of hte habit as json file if provided with a single Habit obj
        if provided with a list of habits stores them into the file "habtrack.json"

    ===== Parameters =====
    hab_element : habit.Habit | list
        the representation that has to be stored to disk
    """
    
    def _file_serialize() -> None:
        """_file_serialize: stores a single habit object"""

        with open(js_file, "w") as file:
            json.dump(hab_element, file, default=_serialize_habit, indent=2)
    
    def _hab_container_serialize() -> None:
        """_hab_container_serialize: stores a list of habits"""

        with open(js_file, "w") as file:
            json.dump(hab_element, file, default=_serialize_habit, indent=2)

    if isinstance(hab_element, src.habit.Habit):
        js_file = data_dir / f"{hab_element.name}.json"
        _file_serialize()

    else:
        js_file = data_dir / "habtrack.json"
        if demo: js_file = data_dir / "sample.json"
        _hab_container_serialize()

# ===== Deserialization ===== #
def _deserialize_habit(dct: dict) -> src.habit.Habit:
    """
    storage._deserialize_habit:
        helper that creates a Habit obj from a given dict

    ===== Parameters =====
    dct : dict
        the dictionary that represents the desired habit object

    ===== Returns =====
    habit.Habit

    ===== Exceptions =====
    TypeError
        if the dict is not a valid Habit obj
    """

    if not "_HABIT" in dct.keys():
        raise TypeError("cant convert dict to habit, not a habit: _HABIT missing")

    def _set_date(ordinal: int) -> datetime.date:
        """returns date from ordinal, created just for better readability"""
        return datetime.date.fromordinal(ordinal)

    hab = src.habit.Habit(
        name=dct["name"],
        description=dct["description"],
        periodicity=dct["periodicity"],
        amount=dct["amount"],)
    hab.creation_date = _set_date(dct["creation_date"])

    for ordinal in dct["checkoffs"]:
        hab.checkoffs.append(_set_date(ordinal))
    
    return hab

def deserialize(file_source: str = None, demo: bool = False) -> list:
    """
    storage.deserialize:
        loads stored json representations from the data directory

        default behavior is to load all habits stored in the file habtrack
        if given a file name and the file exists lods only the given file
        if the demo flag is True it returns the sample habits

    ===== Parameters =====
    file_source : str [optional]
        a specific json file within the data dir
    demo : bool [otional]
        switches to demo mode (returns sample habits)

    ===== Returns =====
    hab_container : list
        list of loaded habits
    """
    
    js_file = data_dir / "habtrack.json"
    if demo: js_file = data_dir / "sample.json"

    if file_source and (data_dir / f"{file_source}.json").exists():
        js_file = data_dir / f"{file_source}.json"

    hab_container = []

    if js_file.exists() and not js_file.stat().st_size == 0:
        with open(js_file, "r") as file:
            for i in json.load(file):
                hab_container.append(_deserialize_habit(i))
    
    return hab_container