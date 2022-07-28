import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[1]))

from habtrack import habit
import json, datetime, pathlib


# ============================================= #
# ============== Derialization ================ #
# ============================================= #
def _serialize_habit(habit: habit.Habit) -> dict:
    """_serialize_habit: helper that creates a dict from a habit.Habit
    
    Parameter
    ---------
    habit : habit.Habit

    Return
    ------
    dict
        dict representation of a habit
    """
    return {
        "_HABIT": True,
        "name": habit.name,
        "description": habit.description,
        "periodicity": habit.periodicity.periodicity,
        "amount_checkoffs": habit.amount_checkoffs,
        "creation_date": habit.creation_date.toordinal(),
        "checkoffs": [check.toordinal() for check in habit.checkoffs]
    }

def serialize_habit(element: habit.Habit | list) -> None:
    """serialize_habit: processes a container of habits of habit and
    stores them as json representation in a json file in the 
    "project_root/dir" location

    if given a single habit, it stores it in a file corresponding to
    the name of habit. IF EXISTING FILE WILL BE REPLACED

    if given an iterable containing habits it will store them all
    into a file called "habtrack.json" in the "project_root/data/" location
    IF EXISTING FILE WILL BE REPLACED

    
    Parameter
    ---------
    element : list | habit.Habit
        list of habits from the current system
    """
    data_dir = pathlib.Path(__file__).parents[1] / "data"

    if isinstance(element, habit.Habit):
        with open(data_dir / f"{element.name}.json", "w") as file:
            json.dump(element , file, default=_serialize_habit, indent=2)
    
    else:
        with open(data_dir / "habtrack.json", "w") as file:
            for hab in element:
                if isinstance(hab, habit.Habit):
                    json.dump(hab, file, default=_serialize_habit, indent=2)
                else:
                    raise TypeError("gicen object is not a valid habit object")



# ============================================= #
# ============== Deserialization ============== #
# ============================================= #
def _deserialize_habit(dct: dict) -> habit.Habit:
    """_deserialize_habit: helper that creates a habit from a dictionary representation of a habit

    in the dictionary representation has to be the item ("__HABIT", True)

    Parameter
    ---------
    dct : dictionary
        the dictionary representation of a habit
    
    Return
    ------
    hab : habit.Habit
        the from the dictionary created habit
    """

    if not "_HABIT" in dct.keys():
        raise TypeError("cant convert dict to habit, not a habit: _HABIT missing")

    def _set_date(ordinal: int) -> datetime.date:
        """returns date from ordinal, just for better readability"""
        return datetime.date.fromordinal(ordinal)

    hab = habit.Habit(
        name=dct["name"],
        description=dct["description"],
        periodicity=dct["periodicity"],
        amount_checkoffs=dct["amount_checkoffs"],)
    hab.creation_date = _set_date(dct["creation_date"])

    for ordinal in dct["checkoffs"]:
        hab.checkoffs.append(_set_date(ordinal))
    
    return hab

def deserialize_js() -> list:
    """deserialize_js: loads all habits that are represented as json in
    the /"root/data" folder

    Returns
    -------
    habbitse : list
        list of habit objects
    """
    data_dir = pathlib.Path(__file__).parents[1] / "data"
    js_files = [i for i in data_dir.iterdir() if i.suffix == ".json"]

    habbitse = []

    for file in js_files:
        with open(file) as js_rep:
            for i in json.load(js_rep):
                habbitse.append(_deserialize_habit(i))
    
    return habbitse