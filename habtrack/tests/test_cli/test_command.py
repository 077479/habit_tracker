"""
module test_command: the test module for the module cli_command

===== Imports =====
built-in:
    unittest.mock.patch
    unittest.mock.Mock
    unittest
    pytest
package-intern:
    cli

===== Classes =====
TestTestCommand(unittest.TestCase):
    the test class for the module cli_command
"""
# ========== - import - ========== #
from unittest.mock import patch, Mock
import pytest, cli, unittest


# ========== - logic - ========== #
class TestCommand(unittest.TestCase):
    
    # ===== setup / teardown ===== #
    @classmethod
    def setUpClass(cls):
        """setup the test environment"""
        cls.fake_hab = Mock()
        cls.fake_hab.name = "fake_hab"

        cls.orig_sys = cli.command.sys
        cls.orig_src_storage = cli.command.src.storage

        cli.command.sys = Mock()
        cli.command.sys.argv = ["", "", "__str__", "-n=test", "-p=weekly"]

        cli.command.src.storage = Mock()
        cli.command.src.storage.deserialize.return_value = [TestCommand.fake_hab]
        cli.command.src.storage.serialize.return_value = "storage"

    @classmethod
    def tearDownClass(cls):
        """reset the mocks to origin"""
        cli.command.sys = TestCommand.orig_sys
        cli.command.src.storage = TestCommand.orig_src_storage


    # ===== init ===== #
    def test_class_init_type(self):
        """test if the class is instantiable without error"""
        assert type(cli.command.Command(False)) == cli.command.Command

    def test_class_init_demo(self):
        """test for the correct assignment of _demo"""
        assert cli.command.Command(False)._demo == False

    def test_class_init_sub_command(self):
        """test of correct assignment of sub_command"""
        assert cli.command.Command(False)._sub_command == "__str__"


    # ===== _get_args ===== #
    def test_get_args_type(self):
        """test type of return"""
        assert type(cli.command.Command(False)._get_args()) == dict

    def test_get_args_args(self):
        """test for correct content of the args"""
        assert cli.command.Command(False)._get_args()["n"] == "test"


    # ===== _get_habits ===== #
    def test_get_habits_type(self):
        """test for correct type"""
        assert type(cli.command.Command(False)._habits) == dict

    def test_get_habits_content(self):
        """test for correct content"""
        assert cli.command.Command(False)._habits["fake_hab"].name == "fake_hab"


    # ===== _get_habit_lst ===== #
    def test_get_habit_lst_type(self):
        """test for correct type"""
        assert type(cli.command.Command(False)._get_habit_lst()) == list

    def test_get_habit_lst_content(self):
        """test for correct content"""
        assert cli.command.Command(False)._get_habit_lst()[0].name == "fake_hab"


    # ===== _store ===== #
    def test_store_call(self):
        """test for the correct call"""
        cli.command.Command(False)._store()
        cli.command.src.storage.serialize.assert_called()


    # ===== _get_success_out ===== #
    def test_get_success_out_content(self):
        """test for the correct print call"""
        with patch("builtins.print") as patch_print:
            cli.command.Command(False)._get_success_out("patch", "called")
        patch_print.assert_called_with("\nDONE, 'patch' is called\n")


    # ===== _get_missing_out ===== #
    def test_get_missing_out_content(self):
        """test for the correct print call"""
        with patch("builtins.print") as patch_print:
            with pytest.raises(SystemExit):
                cli.command.Command(False)._get_missing_out({"-n":None}, "-n")
                # {sub_command}, {args} 
        patch_print.assert_called_with("ERROR!!!\nto perform __str__ the arguments ('-n',) are needed!\nExiting . . .")