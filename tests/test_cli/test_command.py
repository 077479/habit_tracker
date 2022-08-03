# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))


# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli, habtrack, pytest


# ========== - logic - ========== #
@patch.object(sys, 'argv', ["", "", "__str__"])
def test_type_object():
    assert type(cli.command.Command(False)) == cli.command.Command

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_type_attr_1():
    assert type(cli.command.Command(False)._habits) == dict

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_type_attr_2():
    assert cli.command.Command(True)._demo == True
    assert cli.command.Command(False)._demo == False

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_attribute__subcommand():
    assert cli.command.Command(False)._sub_command == "__str__"

@patch.object(sys, 'argv', ["", "", "__str__", "-n", "name"])
def test__get_args():
    assert cli.command.Command(False)._get_args()["n"] == "name"

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_get_habits():
    hab = Mock()
    hab.name = "test"
    
    with patch.object(habtrack.storage, "deserialize", return_value=[hab]):
        assert cli.command.Command(False)._habits["test"].name == "test"

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_get_habit_lst():
    hab = Mock()
    hab.name = "test"
    
    with patch.object(habtrack.storage, "deserialize", return_value=[hab]):
        assert cli.command.Command(False)._get_habit_lst()[0].name == "test"

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_store():
    with patch.object(habtrack.storage, "serialize") as fake_storage:
        cli.command.Command(False)._store()
        assert fake_storage.call_count == 1


@patch.object(sys, 'argv', ["", "", "__str__"])
def test_get_success_out():
    with patch("builtins.print") as fake_print:
        cli.command.Command(False)._get_success_out("Test", "asserted")
        assert fake_print.call_count == 1
        fake_print.assert_called_once()

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_get_missing_out():
    with pytest.raises(SystemExit) as fake_sysexit:
        cli.command.Command(False)._get_missing_out({1:None}, 1)
    assert fake_sysexit.type == SystemExit

@patch.object(sys, 'argv', ["", "", "__str__"])
def test_get_wrong_sub_out():
    with pytest.raises(SystemExit) as fake_sysexit:
        with patch("builtins.print") as fake_print:
            cli.command.Command(False)._get_wrong_sub_out()
            assert fake_print.call_count == 1
            fake_print.assert_called_once()