def get_streaks(habit):
    def set_time_period(start):
        return (period(start, 0), period(start, 1))

    def lst_diff(lst_1, lst_2):
        for i in lst_2:
            if i in lst_1:
                lst_1.remove(i)

    def set_streak_list(checkoffs, time_period, ret_lst, amount_checkoffs):
        added = False
        counter = 0
        for checkoff in checkoffs:
            if time_period[0] <= checkoff <= time_period[1]:
                counter += 1
                ret_lst[-1].append(checkoff)

        if counter >= amount_checkoffs: added=True
        if not added and ret_lst[-1]: ret_lst.append(list())

        lst_diff(checkoffs, ret_lst[-1])
    
    checkoffs = habit.checkoffs.copy()
    period = habit.periodicity
    creation_date = habit.creation_date
    streaks_list = [list()]
    time_period = set_time_period(creation_date)
    amount_checkoffs = period.amount_checkoffs

    while checkoffs:
        set_streak_list(checkoffs, time_period, streaks_list, amount_checkoffs)
        time_period = set_time_period(time_period[1])

    return streaks_list

def get_longest_streak():
    pass

def get_habits_by_period():
    pass

def is_broken():
    pass

def get_longest_streak():
    pass

def list_habits():
    pass

def list_checkoffs(habit):
    print(habit)
    [print(f"  {i}") for i in sorted(habit.checkoffs)]