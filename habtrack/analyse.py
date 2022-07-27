from datetime import date

def get_streaks(habit):
	def set_time_period(start):
		return (period(start, 0), period(start, 1))

	def set_streak_list(checkoffs, time_period, ret_lst, amount_checkoffs):
		added = False
		counter = 0
		for i in checkoffs:
			if time_period[0] <= i <= time_period[1]:
				counter += 1
				ret_lst[-1].append(i)
		
		checkoffs = checkoffs.difference(ret_lst[-1])

		if counter >= amount_checkoffs: added=True
		if not added and ret_lst[-1]: ret_lst.append(list())

		return checkoffs

	checkoffs = habit.checkoffs
	period = habit.periodicity
	creation_date = habit.creation_date
	streaks_list = [list()]
	time_period = set_time_period(creation_date)
	amount_checkoffs = period.amount_checkoffs

	while checkoffs:
		checkoffs = set_streak_list(checkoffs, time_period, streaks_list, amount_checkoffs)
		time_period = set_time_period(time_period[1])
	return streaks_list

def get_longest_streak(habit):
	"""
	TODO handle case when several streaks have the same len
	"""
	longest_streak = list()
	streaks = get_streaks(habit)
	for streak in streaks:
		if len(streak) > len(longest_streak): longest_streak = streak
	return longest_streak

def get_habits_by_period(group, period):
	habits_with_period = list()
	for habit in group:
		if habit.periodicity.periodicity == period:
			habits_with_period.append(habit)
	return habits_with_period

def is_broken(habit):
	time_period = (habit.periodicity(date.today(), -1), habit.periodicity(date.today(), 0))
	for checkoff in habit.checkoffs:
		if time_period[0] < checkoff < time_period[1]:
			return False
	return True

def get_longest_streak_of_habits(group):
	linked_habit = None
	longest_streak = list()

	for habit in group:
		if len(get_longest_streak(habit)) > len(longest_streak):
			longest_streak = get_longest_streak(habit)
			linked_habit = habit

	return (linked_habit, longest_streak)

def list_habits(group):
	for i in group:
		print(i)

def list_checkoffs(habit):
	print(habit)
	checkoffs = sorted(list(habit.checkoffs))
	for checkoff in checkoffs:
		print(f"  {checkoff}")