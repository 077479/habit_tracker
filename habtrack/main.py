from habit import Habit
from period import Period

# ============================================= #
# ================= Habit Mngt ================ #
# ============================================= #
def create_habit(name, description, period):
	return Habit(name=name, description=description, periodicity=period)

def delete_habit(habit, habit_group=None):
	if habit_group:
		for i in habit_group:
			if habit == i: habit_group.remove(i)
	del habit

def check_off(habit):
	habit.check_off()

def change_period(habit, period):
	habit.periodicity = Period(period)

def get_list_of_stored_habits():
	# TODO implement functionality
	pass