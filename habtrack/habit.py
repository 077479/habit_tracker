from datetime import date
from period import Period

class Habit:
	def __init__(self, name, description, periodicity):
		self._HABIT = True
		self.group = None
		self.name = name
		self.description = description
		self.periodicity = Period(periodicity)
		self.creation_date = date.today()
		self.checkoffs = set()

	def check_off(self) -> None:
		self.checkoffs.add(date.today())
	
	def __str__(self):
		return f"Habit: {self.name} | {self.creation_date} | {self.periodicity.periodicity}"
	
	def __eq__(self, other):
		group_eq = self.group == other.group
		name_eq = self.name == other.name
		desc_eq = self.description == other.description
		period_eq = self.periodicity.periodicity == other.periodicity.periodicity
		creat_eq = self.creation_date == other.creation_date
		checkof_eq = self.checkoffs == other.checkoffs
		if name_eq and desc_eq and period_eq and creat_eq and checkof_eq and group_eq:
			return True
		return False