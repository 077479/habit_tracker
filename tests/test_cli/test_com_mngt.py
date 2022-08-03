# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))


# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli

# ========== - logic - ========== #
@patch.object(sys, 'argv', ["", "", "__str__"])
def test_type_object():
    assert type(cli.com_mngt.Mngt(False)) == cli.com_mngt.Mngt

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_check_off():
    pass

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_change_period():
    pass

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_create():
    pass

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_delete_habit():
    pass