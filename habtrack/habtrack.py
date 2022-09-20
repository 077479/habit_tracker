"""
module habtrack: provides the entry point of the tool for the CLI

===== Imports =====
built_in
    pythlib, sys
package-intern
    cli.cli_start

===== Functions =====
run() -> None
    just starts the cli by the call cli.cli_start.CliStart()

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""
# ========== - package import access - ========== #
import pathlib, sys
if not str(pathlib.Path(__file__).parent) in sys.path:
    sys.path.append(str(pathlib.Path(__file__).parent))


# # ========== - import - ========== #
import cli.cli_start

# # ========== - logic - ========== #
def run():
    cli.cli_start.CliStart()

# ===== Entry Point ===== #
if __name__ == "__main__":
    run()