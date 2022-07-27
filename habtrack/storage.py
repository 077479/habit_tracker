from habit import Habit
from datetime import date
from pathlib import Path
import json

# ============================================= #
# =============== Serialization =============== #
# ============================================= #
def _serialize_habit(habit):
	if isinstance(habit, Habit):
		creation_date_serialized = _serialize_date(habit.creation_date)

		checkoffs_serialized = list()
		checkoffs = sorted(list(habit.checkoffs))
		for checkoff in checkoffs:
			checkoffs_serialized.append(_serialize_date(checkoff))

		return {
			"_HABIT": True,
			"name": habit.name,
			"description": habit.description,
			"periodicity": habit.periodicity.periodicity,
			"creation_date": creation_date_serialized,
			"checkoffs": checkoffs_serialized
		}
	raise TypeError("Object given is not a valid Habit")

def _serialize_date(date):
	return {"year":date.year, "month":date.month, "day":date.day}

def serialize_habit(habit, debug=False):
	"""
	TODO differniate between habit and list, every list different json file
	"""
	if debug:
		return json.dumps(habit, default=_serialize_habit, indent=2)

	filepath = Path(Path.cwd() / "data/lst.json")
	with open(filepath, "w") as file:
		file.write(json.dumps(habit, default=_serialize_habit, indent=2))

# ============================================= #
# ============== Deserialization ============== #
# ============================================= #
def _deserialize_habit(dct):
	habit = Habit(dct["name"], dct["description"], dct["periodicity"])
	habit.creation_date = _set_date(dct["creation_date"])
	for checkoff_dict in dct["checkoffs"]:
		habit.checkoffs.add(_set_date(checkoff_dict))
	return habit

def _set_date(date_dct):
	return date(date_dct["year"], date_dct["month"], date_dct["day"])

def deserialize_habit(json_rep, debug=False):
	"""
	return a list with habits even if its just one habit
	"""
	if debug:		
		habit_dct = json.loads(json_rep)
		if "_HABIT" in habit_dct.keys():
			habit = _deserialize_habit(habit_dct)
		else:
			raise Exception("the JSON representation is not a valid Habit")
		return habit

	filepath = Path.cwd() / f"data/{json_rep}"

	with open(filepath, "r") as file:
		hab_dct = json.load(file)

	if "_HABIT" in hab_dct.keys():
		return _deserialize_habit(hab_dct)
	else:
		raise Exception("the JSON representation is not a valid Habit")