"""
module habtrack: provides the entry point of the tool for the CLI

===== Imports =====
package-intern
    cli

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""
# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import cli


# ========== - logic - ========== #
# ===== Entry Point ===== #
if __name__ == "__main__":
    cli.cli_start.CLI_Start()