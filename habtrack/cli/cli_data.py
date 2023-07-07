"""
module cli_data
    provides needed hardwired data

===== Globals =====
info_command : str
    the info to the usage of the command functionality

info_mngt : str
    the info to the usage of the management functionality

info_analyse : str
    the info to the usage of the analyse functionality

info_storage : str
    the info to the usage of the storage functionality

sample : str
    the default hardwired sample data

man : list
    the data for the semi interactive tool introduction
    content is a list with touples
    each tuple containing the printed text as [0]
    and the programflow control data as [1]

reference : str
    the reference of the tool
"""

info_command=r"""  - mngt:         gives accesses to the management category of the functionality
  - analyse:      gives accesses to the analyse category of the functionality
  - storage:      gives accesses to the storage category of the functionality
  - list_habits:  just shows all currently stored habits
  - demo_default: resets the demo data
  - reference:    shows a complete summary of commands, subcommands and options
  - man:          starts a short semi-interactive manual"""

info_mngt=r"""  - create:        creates a new habit (needs the args "-n" and the "-p" as mandatory info)
  - check_off:     marks a habit as done for one day (needs the arg "-n" as mandatory info)
  - change_period: changes teh period of a given habit (needs the args "-n" and the "-p" as mandatory info)
  - delete_habit:  deletes a habit without warning"""

info_analyse=r"""  - get_streaks:                  shows all streaks of a habit (needs the arg "-n")
  - get_longest_streak:           shows the longest streak of a provided habit (needs the arg "-n")
  - get_habity_by_period:         shows all habits stored with the given periodicity (needs "-p")
  - is_broken:                    shows if the given habit was fullfilled the last time period (needs "-n")
  - get_longest_streak_of_habits: shows teh habit with the longest streak of all of all stored
  - list_checkoffs:               shows all the dates of checkoffs for a given habit (needs the arg "-n")
  - list_habits:                  shows all habits stored (same as 'habtrack man')"""

info_storage=r"""  - serialize: exports a given habit as json (needs the arg "-n")"""

sample=r"""[
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

man=[
(r"""Hello, this is the manual of the habit tracking tool called habtrack
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    \_\      | Hello iam Habclap,        |
   (_**)     | i will guide you through  |
  __) #_     | this tour                 |
 ( )...()    |                           |
 || | | |    |iam glad that you are here!|
 || | |()__/ |_ _ _ _ _ _ _ _ _ _ _  _ _ |     
 /\(___)
_-"'"'"'"'-_
-,,,,,,,,- 

this manual is designed as semi-interactive experience
if you want to stop, just use "[ctl]+c" or "[ctl]+z"

if this is too much, there is for every command category of this tool a vialble help option
that gives a short description of what which command does

to access the help: "habtrack help" or "habtrack [command] help"

""", False),

(r"""the developer - just one guy who not that randomly learned python and now calls himself 
    that - but who am i to decide (; - of this tool has decieded to split up the 
    functionality into commands and subcommands

              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | this scheme is maybe (totally)|
   (_**)     | inspired by tools like git    |
  __) #_     | but lets go on with the tour  |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

 the general usage of it is:
    "habtrack [demo flag (optional)] [command] [sub-command] [options]"

""", False),

(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | lets go through it together   |
   (_**)     |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
  __) #_     

    "habtrack [demo flag (optional)] [command] [sub-command] [options]"

    - "habtrack":
        the 'starter' python file of the CLI for the tool

    - "demo flag": the tool provides a demo-mode,
        - in the "demo mode" sample data is provided to explore the abilities of the tool
        - the demo flag is optional and the demo-mode only starts when the "--demo" is provided
        - the demoflag can be given anywhere, unlike the commands and sub-commands it is not bound to a position
        - e.g.1: habtrack --demo [command] [subcommand] [options] is fine
        - e.g.2: habtrack [command] [subcommand] --demo [options] is totally fine too

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

""", "habtrack help"),

(r"""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | hmmh seems obvious, but what    |
   (_**)     | if i want to know a subcommand  |
  __) #_     | of, lets see . . . "analyse"    |
             | lets try this!                  |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

""", "habtrack analyse help"),

(r"""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | at least it is discriptive, |
   (_**)     | even if the names arent as  |
  __) #_     | good as they are descriptive|
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

(r"""              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
             | but lets be honest here, you are|
             | probably thinking "i will never |
             | remember all the commands, sub- |
             | commands and options            |
    \_\      |                                 |
   (_**)     | the developer told me that      |
  __) #_     | he was struggling with the      |
             | cli design too                  |
             |                                 |
             | and has provided a hardwired    |
             | reference                       |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[the idea for that came from a (highly recommandable)
talk of Daniele Procida (core developer of Django)
during the PyCon 2017]

[so lets try it out]:

""", "habtrack reference"),

(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | nice now that we knew the gist of it  |
   (_**)     | lets test the workflow, with the above|
  __) #_     | so often mentioned (at least 9 times  |
             | on 5 lines to the demo-flag) demo-mode|
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[first lets make sure the demo data is clean, so we call
the "demo_default" command]

""", "habtrack demo_default"),

(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | ha we get the response that its done  |
   (_**)     |                                       |
  __) #_     | now the demo-data is created and      |
             | stored in the file                    |
             | project-root/data/sample.json         |
             |                                       |
             | by the way every habtrack command     |
             | gives a response if it was done or    |
             | not                                   |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

[lets take a look at the sample data 
(and here we go again demo, demo, demo demo demo demr dfeom . . .)
let us just make the call and dont talk about demo related things again]

""", "habtrack --demo list_habits"),

(r"""
lets take one and look closer to it

[Habit: vacuum_clean | 2000-01-01 | weekly | amount: 3]

Habit: vacuum_clean => the name of the habit
2000-01-01 => the creation date of the habit (year-month-day)
weekly => the periodicity of the habit
amount: 3 => the amount of "check_offs" needed in order to be fullfilled

(much words to say "vacuum_clean the apartment 3 times a week")

""", False),

(r"""
[lets check if something was done lately]
""", "habtrack --demo analyse is_broken -n=pay_rent"),
(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | oh . . .                      |
   (_**)     |                               |
  __) #_     | that does not sound good      |
             | lets check how many rents are |
             | due                           |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

""", "habtrack --demo analyse list_checkoffs -n=pay_rent"),

(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | oh no                         |
   (_**)     |                               |
  __) #_     | last paid rent 2000-08-01     |
             | i think we are in trouble     |
             |                               |
             | lets do something about it    |
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

""", "habtrack --demo mngt check_off -n=pay_rent"),

(r"""
              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    \_\      | puh                           |
   (_**)     | that should buy us            |
  __) #_     | a month worth of time         |
             |                               |
             | But enough with this demo work|
             |                               |
             | lets do something new         |
             | i always wanted to take piano |
             | lessons so lets create a habit|
             |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

""", 'habtrack mngt create -n=piano_lessons -p=weekly -d="i want to be elton john" -a=14'),

(r"""
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

reference=r"""
- [command]: 
    With Subcommands:
        - [mngt] - access the "management" functionality for the tool
        - [analyse] - access the "analyse" functionality for the tool
        - [storage] - access the "storage"(limited to one action) functionality for the tool
    Without Subcommands:
        - [list_habits] - convinience call to list all stored habits
        - [demo_default] - restores the default sample habits for the "demo mode" (resets the demo mode)
        - [reference] - shows a summarization of the tool
        - [man] - this screen
    e.g. 1 : habtrack mngt create -n="make Tea" -p="daily"
    e.g. 2 : habtrack analyse get_streaks -n="make Tea"
    e.g. 3 : habtrack man

- [subcommand]:
    - access to the functionality of the commands
    - dont fear, the options seen here will be discussed in the "[options]" section, but are shown here for the completion

    [mngt]:
        - [create] takes (-n(ame), -p(eriod), [-d(iscription)-optional], [-a(mount)-optional]) => creates a habit and stores it
        - [check_off] takes (-n(ame)) => checks off the given habit (mark it as done one time for today)
        - [change_period] takes (-n(ame), -p(eriod)) => changes the period of the given habit
        - [delete_habit] takes (-n(ame)) => deletes the given habit, without warning

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
        - [-a(mount)] => the amount a habit has to be done within its "period" to represent one time, twice, and so on
"""