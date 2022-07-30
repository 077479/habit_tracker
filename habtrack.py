# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))


# ========== - import - ========== #
import habtrack


# ========== - logic - ========== #


print(help(habtrack.period.Period))