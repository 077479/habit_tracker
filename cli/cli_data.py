"""
module cli_data: provides needed hardwired data

===== Globals =====
sample : str
    the default sample data

man : str
    the manual for the tool
"""
info_command="""  - mngt:         gives accesses to the management category of the functionality
  - analyse:      gives accesses to the analyse category of the functionality
  - storage:      gives accesses to the storage category of the functionality
  - list_habits:  just shows all currently stored habits
  - demo_default: resets the demo data
  - reference:    shows a complete summary of commands, subcommands and options
  - man:          starts a short semi-interactive manual"""

info_mngt = """  - create:        creates a new habit (needs the args "-n" and the "-p" as mandatory info)
  - check_off:     marks a habit as done for one day (needs the arg "-n" as mandatory info)
  - change_period: changes teh period of a given habit (needs the args "-n" and the "-p" as mandatory info)
  - delete_habit:  deletes a habit without warning"""

info_analyse="""  - get_streaks:                  shows all streaks of a habit (needs the arg "-n")
  - get_longest_streak:           shows the longest streak of a provided habit (needs the arg "-n")
  - get_habity_by_period:         shows all habits stored with the given periodicity (needs "-p")
  - is_broken:                    shows if the given habit was fullfilled the last time period (needs "-n")
  - get_longest_streak_of_habits: shows teh habit with the longest streak of all of all stored
  - list_checkoffs:               shows all the dates of checkoffs for a given habit (needs the arg "-n")
  - list_habits:                  shows all habits stored (same as 'python habtrack.py man')"""

info_storage="""  - serialize: exports a given habit as json (needs the arg "-n")"""

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

man = [
("""Hello, this is the manual of the habit tracking tool called habtrack
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    \_\      | Hello iam Habclap,        |
   (_**)     | i will guide you through  |
  __) #_     | this tour                 |
 ( )...()    |                           |
 || | | |    |iam glad that you are here!|
 || | |()__/ |_ _ _ _ _ _ _ _ _ _ _  _ _ |     
 /\(___)
_-"\"\"\"\"\"\"-_
-,,,,,,,,- 

this manual is designed as semi-interactive experience
if you want to stop, just use "[ctl]+c" or "[ctl]+z"

if this is too much, there is for every command category of this tool a vialble help option
that gives a short description of what which command does

to access the help: "python habtrack.py help" or "python habtrack.py [command] help"
""", False),

("""the developer - just one guy who randomly learned to python and now calls himself 
    that but who am i to decide (; - of this tool has decieded to split up the 
    functionality into commands and subcommands

              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | this scheme is maybe (totally)|
   (_**)     | inspired by tools like git    |
  __) #_     | but lets go on with the tour  |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

 the general usage of it is:
    "python habtrack.py [demo flag (optional)] [command] [sub-command] [options]"
""", False),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | lets go through it together   |
   (_**)     |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
  __) #_     

    "python habtrack.py [demo flag (optional)] [command] [sub-command] [options]"
    
    - "python":
        the call to the python interpreter

    - "habtrack.py":
        the 'starter' python file of the CLI for the tool

    - "demo flag": the tool provides a demo-mode,
        - in the "demo mode" sample data is provided to explore the abilities of the tool
        - the demo flag is optional and the demo-mode only starts when the "--demo" is provided
        - the demoflag can be given anywhere, unlike the commands and sub-commands it is not bound to a position
        - e.g.1: python habtrack.py --demo [command] [subcommand] [options] is fine
        - e.g.2: python habtrack.py [command] [subcommand] --demo [options] is totally fine too

    - [command]:
        the command gives access to the categorized functionality
        the categories are:
            - mngt(management)
            - analyse(to show off the data)
            - storage(to export the data)
    
    - [sub-command]:
        subcommands are command specific and we will go through them in a moment
    
    [but lets try a "help call". . .]
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | let me take care of that      |
   (_**)     | you can relax for a bit, and i|
  __) #_     | will do the work this time    |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

""", "python habtrack.py help"),

("""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | hmmh seems obvious, but what    |
   (_**)     | if i want to know the subcommand|
  __) #_     | of, lets see . . . "analyse"    |
             | lets try this!                  |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
""", "python habtrack.py analyse help"),

("""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | at least it is discriptive, |
   (_**)     | even if the names arent as  |
  __) #_     | good as descriptive         |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

but lets step back here and lets talk about
optional arguments

optional arguments are there to provide neccessary information needed
in order to carry out the subcommand

but fear not, there are only 4

  - [-n(name)] => represents the name of a habit (shown in the list all habits function)
  - [-p(eriod)] => represents the periodicity of a habit can be:
    - [daily] => every day
    - [weekly] => every week
    - [monthly] => every month
  - [-d(escription)] => a brief description of the habit
  - [a(mount)] => the amount a habit has to be done within its "period" to represent one time, twice, and so on
""", False),

("""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | but lets be honest here, you are|
   (_**)     | probably thinking "i will never |
  __) #_     | remember all the commands, sub- |
             | commands and options            |
             |                                 |
             | the developer told me that      |
             | he was struggling  with the     |
             | cli design                      |
             |                                 |
             | and has provided a harwired     |
             | reference                       |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[the idea for that came from a (highly recommandable)
talk of Daniele Procida (core developer of Django)
during the PyCon 2017]

[so lets try it out]:
""", "python habtrack.py reference"),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | nice now that we knew the gist of it  |
   (_**)     | lets test the workflow, with the above|
  __) #_     | so often mentioned (at least 9 times  |
             | on 5 lines to the demo-flag) demo-mode|
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[first lets make sure the demo data is clean, so we call
the "demo_default" command]

""", "python habtrack.py demo_default"),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | ha we get the response that its done  |
   (_**)     |                                       |
  __) #_     | now the demo-data is created and      |
             | stored in the file                    |
             | project-root/data/sample.json         |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[lets take a look at the sample data (i refuse to say the de#"-*ode) phrase one more time
but besides that lets make the call]
""", "python habtrack.py --demo list_habits"),

("""
lets take one and look closer to it

[Habit: vacuum_clean | 2000-01-01 | weekly | amount: 3]

Habit: vacuum_clean => the name of the habit
2000-01-01 => the creation date of the habit (year-month-day)
weekly => the periodicity of the habit
amount: 3 => the amount of "check_offs" needed in order to be fullfilled
(much words to say "vacuum_clean the apartment 3 times a week")
""", False),

("""
[lets check if something was done lately]
""", "python habtrack.py --demo analyse is_broken -n=pay_rent"),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | oh . . .                      |
   (_**)     |                               |
  __) #_     | that does not sound good      |
             | lets check how many rents are |
             | due                           |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
""", "python habtrack.py --demo analyse list_checkoffs -n=pay_rent"),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | oh no                         |
   (_**)     |                               |
  __) #_     | last paid rent 2000-08-01     |
             | i think we are in trouble     |
             |                               |
             | lets do something about it    |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
""", "python habtrack.py --demo mngt check_off -n=pay_rent"),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | that should buy us a month    |
   (_**)     | worth of time                 |
  __) #_     |                               |
             | But enough with this demo work|
             |                               |
             | lets do something new         |
             | i always wanted to take piano |
             | lessons so lets create a habit|
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
""", 'python habtrack.py mngt create -n=piano_lessons -p=weekly -d="i want to be elton john" -a=76'),

("""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | now i will tend to my piano lessons |
   (_**)     | i have a lot to do                  |
  __) #_     |                                     |
             | But i have trust that you have      |
             | learned enough to get around with   |
             | this tool                           |
             |                                     |
             | so til the next time                |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
""", False)]

reference="""
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
"""