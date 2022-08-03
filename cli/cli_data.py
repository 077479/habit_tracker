"""
module cli_data: provides needed hardwired data

===== Globals =====
sample : str
    the default sample data

man : str
    the manual for the tool
"""

sample = """[
        {
            "_HABIT":true,
            "name":"work",
            "description":"daily[1], Streaks[2] 4/4",
            "periodicity":"daily",
            "amount":1,
            "creation_date":730120,
            "checkoffs": [
                730120,
                730121,
                730122,
                730123,
                730125,
                730126,
                730127,
                730128
            ]
        },
        {
            "_HABIT":true,
            "name":"eat",
            "description":"daily[2], Streaks[4] 2/4/1/1",
            "periodicity":"daily",
            "amount":2,
            "creation_date":730120,
            "checkoffs": [
                730120,
                730120,
                730122,
                730122,
                730123,
                730123,
                730125,
                730126
            ]
        },
        {
            "_HABIT":true,
            "name":"swimming",
            "description":"weekly[1], Streaks[3] 2/2/4",
            "periodicity":"weekly",
            "amount":1,
            "creation_date":730120,
            "checkoffs": [
                730123,
                730129,
                730141,
                730146,
                730161,
                730165,
                730167,
                730172
            ]
        },
        { 
            "_HABIT":true,
            "name":"vacuum_clean",
            "description":"weekly[3], Streaks[3] 5/2/1",
            "periodicity":"weekly",
            "amount":3,
            "creation_date":730120,
            "checkoffs": [
                730122,
                730124,
                730126,
                730128,
                730131,
                730142,
                730146,
                730156
            ]
        },
        {
            "_HABIT":true,
            "name":"pay_rent",
            "description":"monthly[1], Streaks[1] 8",
            "periodicity":"monthly",
            "amount":1,
            "creation_date":730120,
            "checkoffs": [
                730120,
                730151,
                730180,
                730211,
                730241,
                730272,
                730302,
                730333
            ]
        },
        {
            "_HABIT":true,
            "name":"shop",
            "description":"monthly[4], Streaks[1] 8",
            "periodicity":"monthly",
            "amount":4,
            "creation_date":730120,
            "checkoffs": [
                730120,
                730128,
                730135,
                730148,
                730150,
                730156,
                730163,
                730172
            ]
        }
    ]"""

man = """
this is the manual for the CLI of the habit tracker tool "habtrack"
the tool works with commands and subcommands

[USAGE]
it is used the following: "python habtrack.py [demo flag (optional)] [command] [subcommand] [options]"

[reference]
lets go through it together:
    - "python": the call to the python interpreter

    - "habtrack.py": the 'starter' python file of the CLI for the tool

    - "demo flag": the tool provides a demo mode, in the "demo mode" sample data is provided and can be changed with the abilities of the tool
        - the demo flag is optional and the tool only starts the "demo mode" if after the "habtrack.py" statement "--demo" is stated
        - e.g.: python habtrack.py --demo [command] [subcommand] [options]

    - [command]: 
        With Subcommands:
            - [mngt] - access the "management" functionality for the tool
            - [analyse] - access the "analyse" functionality for the tool
            - [storage] - access the "storage"(limited to one action) functionality for the tool
        Without Subcommands:
            - [list_habits] - convinience call to list all stored habits
            - [demo_default] - restores the default sample habits for the "demo mode" (resets the demo mode)
            - [man] - this screen
        e.g. 1 : python habtrack.py mngt create -n="make Tea" -p="daily"
        e.g. 2 : python habtrack.py analyse get_streaks -n="make Tea"
        e.g. 3 : python habtrack.py man

    - [subcommand]:
        - access to the functionality of the commands
        - dont fear, the options seen here will be discussed in the "[options]" section, but are shown here for the completion

        [mngt]:
            - [create] takes (-n(ame), -p(eriod), [-d(iscription)-optional], [-a(mount)-optional]) => creates a habit and stores it
            - [check_off] takes (-n(ame)) => checks off the given habit (mark it as done one time for today)
            - [change_period] takes (-n(ame), -p(eriod)) => changes the period of the given habit
            - [delete] takes (-n(ame)) => deletes the given habit, without warning

        [analyse]:
            - [get_habits_by_period] takes (-n(ame), -p(eriod)) => returns all stored habits with the given period
            - [get_longest_streak] takes (-n(ame)) => shows the longest time a habit was done within its time-period
            - [get_longest_streak_of_habits] => shows the Habit with the longest streak of all stored habtis (streak is shown too)
            - [get_streaks] takes (-n(ame)) => shows all streaks of a given habit
            - [is_broken] takes (-n(ame)) => shows if a habit was done in his last time period
            - [list_checkoffs] takes (-n(ame)) => schows all check-offs of a given habit
            - [list_habits] => shows all stored habits
        
        [storage]
            - [serialize] takes (-n(ame)) => creates a data file with only the specified habit stored, if you want to take it with you (;

        - [options]:
            - the options are the parameters that the functionality needs to work
            - in general there are four different ones
            - [-n(name)] => represents the name of a habit (shown in the list all habits function)
            - [-p(eriod)] => represents the periodicity of a habit:
                - [daily] => every day
                - [weekly] => every week
                - [monthly] => every montj
            - [-d(escription)] => a brief description of the habit
            - [a(mount)] => the amount a habit has to be done within its "period" to represent one time, twice, and so on
[Workflow]
lets try something out:
    1. sample data
        - to ensure that the sample data for the "demo mode" is accessable lets just run it one time
        - >>> python habtrack.py demo_default`
        - now a file is created in the data folder with the sample data
    2. list sample data
        - lets take a look at the samplles
        >>> python habtrack.py --demo list_habits
        >>> stored Habits:
        >>>     Habit: work | 2000-01-01 | daily | amount: 1
        - Habit: work => represents the name of the habit the name here is "work"
        - 2000-01-01 => represents the creation date of the habit here the first january 2000
        - daily => represents that this should be done in a daily time period
        - amount: 1 => shows that it should be done one time in his "daily" time period
    3. check if the habit is broken
        - lets look if any of theese habits were done in the last time
        >>> python habtrack.py --demo analyse is_broken -n=pay_rent
        >>> the Habit: 'pay_rent' is currently: broken
        - hmmh that does not seem good
    4. list the checkoffs
        - lets look at how many rents we have missed
        - lets only look at the last entry
        >>> python habtrack.py --demo analyse list_checkoffs -n=pay_rent
        >>> 2020-08-01
        - uhh we are due since august 2020, that cant be good
    5. check off a habit
        - lets change the pay_rent thing, honestly iam concerned
        >>> python habtrack.py --demo mngt check_off -n=pay_rent
        >>> DONE, 'pay_rent' is checked for today
        - puh that should do it for this month
"""