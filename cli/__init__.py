"""
Package cli: the packageprovides the CLI to the habit tracking tool habtrack

===== Imports in init =====
package-intern:
    cli_start

===== Functions =====

===== Dependencies =====
created and tested with "pytest 7.1.2" and "Python 3.10.5
"""

# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import cli_start