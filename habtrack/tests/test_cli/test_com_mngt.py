"""
module test_com_mngt: the test module for the module cli.com_mngt

===== Imports =====
built-in:
    unittest.mock.patch
    unittest.mock.Mock
    unittest
package-intern:
    cli

===== Classes =====
TestMngt(unittest.TestCase):
    the test class for the module cli.com_mngt
"""
# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli, unittest


# ========== - logic - ========== #
class TestMngt(unittest.TestCase):

    # ===== setup / teardown ===== #
    @classmethod
    def setUpClass(cls):    
        """setup the test environment"""
        cls.fake_hab = Mock()
        cls.fake_hab.name = "fake_hab"

        cls.orig_sys = cli.command.sys
        cls.orig_src_storage = cli.command.src.storage

        cls.orig_src_main = cli.com_mngt.src.main

        cli.command.sys = Mock()
        cli.command.sys.argv = ["", "", "__str__", "-n=fake_hab", "-p=weekly"]

        cli.command.src.storage = Mock()
        cli.command.src.storage.deserialize.return_value = [TestMngt.fake_hab]

        cli.com_mngt.src.main = Mock()
        cli.com_mngt.src.main.create_habit.return_value = "create"
        cli.com_mngt.src.main.check_off.return_value = "check_off"
        cli.com_mngt.src.main.change_period.return_value = "change_period"
    
    @classmethod
    def tearDownClass(cls):
        """teardown the mocks"""
        cli.command.sys = TestMngt.orig_sys
        cli.command.src.storage = TestMngt.orig_src_storage
        cli.com_mngt.src.main = TestMngt.orig_src_main

    # ===== init ===== #
    def test_class_init_type(self):
        """check for turning it on"""
        assert type(cli.com_mngt.Mngt(False)) == cli.com_mngt.Mngt


    # ===== create ===== #
    def test_create_call(self):
        """check fr correct call"""
        with patch.object(cli.command.sys, "argv", ["", "", "__str__", "-n=test", "-p=weekly"]):
            cli.com_mngt.Mngt(False).create()
            cli.com_mngt.src.main.create_habit.assert_called_with(name="test", periodicity="weekly", description="", amount=1)

    
    # ===== check_off ===== #
    def test_check_off_call(self):
        """check for correct call"""
        cli.com_mngt.Mngt(False).check_off()
        cli.com_mngt.src.main.check_off.assert_called(TestMngt.fake_hab)


    # ===== change_period ===== #
    def test_check_off_call(self):
        """check for correct call"""
        cli.com_mngt.Mngt(False).change_period()
        cli.com_mngt.src.main.change_period.assert_called_with(TestMngt.fake_hab, "weekly")


    # ===== delete ===== #
    def test_delete_habit_contanier(self):
        test_obj = cli.com_mngt.Mngt(False)
        test_obj.delete_habit()
        assert len(test_obj._habits) == 0