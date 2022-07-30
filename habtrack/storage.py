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
        with open(data_dir / "habtrack.json", "w") as file:
            json.dump(hab_element, file, default=_serialize_habit, indent=2)

    if isinstance(hab_element, habit.Habit):
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

def deserialize(file_source: str = None, demo: bool = False) -> list:
    
    js_file = data_dir / "habtrack.json"
    if demo: js_file = data_dir / "sample.json"

    if file_source and (data_dir / f"{file_source}.json").exists():
        js_file = data_dir / f"{file_source}.json"

    hab_container = []

    with open(js_file, "r") as file:
        for i in json.load(file):
            hab_container.append(_deserialize_habit(i))
    
    return hab_container