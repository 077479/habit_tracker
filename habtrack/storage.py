# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habit
import json, datetime


# ========== - logic - ========== #
data_dir = pathlib.Path(__file__).parents[1] / "data"

# ===== Serialization ===== #
def _serialize_habit(hab: habit.Habit) -> dict:

    return {
        "_HABIT": True,
        "name": hab.name,
        "description": hab.description,
        "periodicity": hab.periodicity.period,
        "amount": hab.amount,
        "creation_date": hab.creation_date.toordinal(),
        "checkoffs": [check.toordinal() for check in hab.checkoffs]
    }

def serialize(hab_element: habit.Habit | list) -> None:

    def _file_serialize() -> None:
        with open(data_dir / f"{hab_element.name}.json", "w") as file:
            json.dump(hab_element , file, default=_serialize_habit, indent=2)
    
    def _hab_container_serialize() -> None:
        with open(data_dir / "habbitse.json", "w") as file:
            for hab in hab_element:
                json.dump(hab, file, default=_serialize_habit, indent=2)

    if hab_element.__module__ == "habit":
        _file_serialize()
    else:
        _hab_container_serialize()

# ===== Deserialization ===== #
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
        amount=dct["amount"],)
    hab.creation_date = _set_date(dct["creation_date"])

    for ordinal in dct["checkoffs"]:
        hab.checkoffs.append(_set_date(ordinal))
    
    return hab

def deserialize(file_source: str, demo: bool = False) -> list:

    js_files = [i for i in data_dir.iterdir() if i.suffix == ".json"]
    
    if pathlib.Path(__file__).parents[1] / "data/sample.json" in js_files:
        js_files.remove(pathlib.Path(__file__).parents[1] / "data/sample.json")

    if demo: js_files = pathlib.Path(__file__).parents[1] / "data/sample.json"
    
    hab_container = []

    for file in js_files:
        with open(file) as js_rep:
            for i in json.load(js_rep):
                hab_container.append(_deserialize_habit(i))
    
    return hab_container