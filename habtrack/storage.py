import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))

import habit
import json, datetime, pathlib


# ============================================= #
# ============== Serialization ================ #
# ============================================= #
def _serialize_habit(habit: habit.Habit) -> dict:

    return {
        "_HABIT": True,
        "name": habit.name,
        "description": habit.description,
        "periodicity": habit.periodicity.periodicity,
        "amount_checkoffs": habit.amount_checkoffs,
        "creation_date": habit.creation_date.toordinal(),
        "checkoffs": [check.toordinal() for check in habit.checkoffs]
    }

def serialize(element: habit.Habit | list) -> None:

    data_dir = pathlib.Path(__file__).parents[1] / "data"

    if isinstance(element, habit.Habit):
        with open(data_dir / f"{element.name}.json", "w") as file:
            json.dump(element , file, default=_serialize_habit, indent=2)
    
    else:
        with open(data_dir / "habbitse.json", "w") as file:
            for hab in element:
                if isinstance(hab, habit.Habit):
                    json.dump(hab, file, default=_serialize_habit, indent=2)
                else:
                    raise TypeError("gicen object is not a valid habit object")



# ============================================= #
# ============== Deserialization ============== #
# ============================================= #
def _deserialize_habit(dct: dict) -> habit.Habit:

    if not "_HABIT" in dct.keys():
        raise TypeError("cant convert dict to habit, not a habit: _HABIT missing")

    def _set_date(ordinal: int) -> datetime.date:
        """returns date from ordinal, created just for better readability"""
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

def deserialize(file_source: str, demo: bool = False) -> list:

    data_dir = pathlib.Path(__file__).parents[1] / "data"
    js_files = [i for i in data_dir.iterdir() if i.suffix == ".json"]
    
    if pathlib.Path(__file__).parents[1] / "data/sample.json" in js_files:
        js_files.remove(pathlib.Path(__file__).parents[1] / "data/sample.json")

    if demo: js_files = pathlib.Path(__file__).parents[1] / "data/sample.json"
    

    habbitse = []

    for file in js_files:
        with open(file) as js_rep:
            for i in json.load(js_rep):
                habbitse.append(_deserialize_habit(i))
    
    return habbitse