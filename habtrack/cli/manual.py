"""
module manual.py: this module provides a short manual where a user can learn how to use the cli

it gets the manual (list with tuple) from cli_data
and works thourgh it one by one,
the first element of the tuple is the manual, the second
provides system calls that will be run through subcommand
to demonstrate the information provided


===== Imports =====
built-ins
    subprocess
    platform
    time
    sys
package-intern
    cli

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

import subprocess, platform, time, sys
from cli import cli_data

def wait_key() -> None:
    """
    wait_key: stops the terminal and prompts for the "enter-key"
    """

    print()
    if platform.system() == "windows":
        subprocess.run("pause", shell=True)
    else:
        subprocess.run('read -p "press enter to continue ..."', shell=True)
    print()

def print_slow(arg_str: str, speed: float) -> None:
    """
    print_slow:
        prints given string to the stdout
        makes a pause for the time given by
        the second arg to imitate 80s SciFy
    
    ===== Parameters =====
    arg_str : str
        the string to be printed
    speed : float
        the speed for printing
    """

    for char in arg_str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def run_shell(arg_str: str, speed: float) -> None:
    """
    run_shell: 
        prints out to screen and runs the given
        str as command in the subrocess.run

    ===== Parameters =====
    arg_str : str
        the string to be printed
    speed : float
        the speed for printing
    """

    sys.stdout.write("habclap@habtrack$ ")
    for char in arg_str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    subprocess.run(arg_str, shell = True)

def man_gen() -> str:
    """
    man_gen: creates the generator for the manual
    """
    for i in cli_data.man:
        yield i

def run():
    """
    run: the entry point of the semi-interactive manual
    """
    
    gen = man_gen()
    try:
        while True:
            elem = next(gen)
            print_slow(elem[0], 0.01)
            if elem[1]: 
                wait_key()
                run_shell(elem[1], 0.25)
            wait_key()            
    except (StopIteration, KeyboardInterrupt):
        pass