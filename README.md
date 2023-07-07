# habtrack
- python dependent tool to track and manage habits

# Install
## requires
- **git**
- **python**
- **pip**
## Virtual Python Environment
- the tool does not rely on third party modules, so it should be safe to install it without a virtual environment, without creating dependency conflicts. so this step can be left out, but for the sake of completeness the steps:

- **create a virtual environment**:
    - ``python -m venv env_habit_tracker``
    - ``cd env_habit_tracker``
- **activate the virtual environment**:
    - **Windows**:
        - ``.\Scripts\activate``
    - **Linux**:
        - ``./bin/activate``
> to deactivate just type ``deactivate``

## Clone
- **clone the repo from github**:
    - ``git clone https://github.com/077479/habit_tracker.git``

## Install
- **change directory to the location of the wheel**:
    - windows:
        - ``cd habit_tracker\wheel``
    - Linux:
        - ``cd habit_tracker/wheel``
- **install with pip**:
    - ``pip install habtrack-1.0-py3-none-any.whl``

# Usage
- after installation it is aviable as the command "*habtrack*" as long the virtual env is activated
- every command/subcommand has a help option: ``habtrack [command] [subcommand] help``
- a reference can be accessed with: ``habtrack reference``
- a semi interactive exploration of the tool is started with: ``habtrack man``
## general Usage
- ``habtrack [command] [subcommand] [options]``
## [command]: 
- With Subcommands:
    - **[mngt]** - access the "management" functionality for the tool
    - **[analyse]** - access the "analyse" functionality for the tool
    - **[storage]** - access the "storage"(limited to one action) functionality for the tool
- Without Subcommands:
    - **[list_habits]** - convinience call to list all stored habits
    - **[demo_default]** - restores the default sample habits for the "demo mode" (resets the demo mode)
    - **[reference]** - shows a summarization of the tool
    - **[man]** - semi interactive exploration of the tool
- e.g. 1 : ``habtrack mngt create -n="make Tea" -p="daily"``
- e.g. 2 : ``habtrack analyse get_streaks -n="make Tea"``
- e.g. 3 : ``habtrack man``

## [subcommand]:
- access to the functionality of the commands
- dont fear, the options seen here will be discussed in the "[options]" section, but are shown here for the completion

- **[mngt]**:
    - **[create]** - takes (-n(ame), -p(eriod), [-d(iscription)-optional], [-a(mount)-optional]) => creates a habit and stores it
    - **[check_off]** - takes (-n(ame)) => checks off the given habit (mark it as done one time for today)
    - **[change_period]** - takes (-n(ame), -p(eriod)) => changes the period of the given habit
    - **[delete_habit]** - takes (-n(ame)) => deletes the given habit, without warning

- **[analyse]**
    - **[get_habits_by_period]** - takes (-n(ame), -p(eriod)) => returns all stored habits with the given period
    - **[get_longest_streak]** - takes (-n(ame)) => shows the longest time a habit was done within its time-period
    - **[get_longest_streak_of_habits]** - shows the Habit with the longest streak of all stored habtis (streak is shown too)
    - **[get_streaks]** - takes (-n(ame)) => shows all streaks of a given habit
    - **[is_broken]** - takes (-n(ame)) => shows if a habit was done in his last time period
    - **[list_checkoffs]** - takes (-n(ame)) => schows all check-offs of a given habit
    - **[list_habits]** - shows all stored habits
    
- **[storage]**
    - **[serialize]** - takes (-n(ame)) => creates a data file with only the specified habit stored, if you want to take it with you (;

- **[options]**
    - the options are the parameters that the functionality needs to work
    - in general there are four different ones
    - **[-n(name)]** => represents the name of a habit (shown in the list all habits function)
    - **[-p(eriod)]** => represents the periodicity of a habit:
        - **[daily]** => every day
        - **[weekly]** => every week
        - **[monthly]** => every montj
    - **[-d(escription)]** => a brief description of the habit
    - **[-a(mount)]** => the amount a habit has to be done within its "period" to represent one time, twice, and so on