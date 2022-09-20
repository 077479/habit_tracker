"""
Package habtrack.cli
    package to provide a cli to use the tool from command line

    cli is created with a form of state pattern
    access to the different functionality through different states

===== Modules =====
cli_data
    storage for data stored as top level references to strings
cli_start
    entry point for the cli
command
    parent class for the commands
com_analyse
    command to access the analyse functionality
com_mngt
    command to access the management functionality
com_storage
    command to access the storage functionality
manual
    access to a short semi interactive introduction

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""