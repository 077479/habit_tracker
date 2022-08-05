# ========== - import - ========== #
from unittest.mock import Mock, patch
import pytest, unittest, cli

# ========== - logic - ========== #
class TestCliStart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """setup the test environment"""
        cls.orig_sys = cli.cli_start.sys
        cls.orig_analyse = cli.cli_start.com_analyse
        cls.orig_storage = cli.cli_start.com_storage
        cls.orig_mngt = cli.cli_start.com_mngt
        cls.orig_data = cli.cli_start.cli_data
        cls.orig_habtrack = cli.cli_start.habtrack

        cli.cli_start.com_analyse = Mock()
        cli.cli_start.com_storage = Mock()
        cli.cli_start.com_mngt = Mock()
        cli.cli_start.cli_data = Mock()
        cli.cli_start.cli_data.man = "man"

        cli.cli_start.habtrack = Mock()



    # ===== - init - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "__str__"])
    def test_init_type(self):
        """test if it turns on"""
        type(cli.cli_start.CliStart()) == cli.cli_start.CliStart

    @patch.object(cli.cli_start.sys, "argv", ["", "--demo", "__str__"])
    def test_init_demo(self):
        """test initial val"""
        assert cli.cli_start.CliStart().demo == True

    # ===== - mngt - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "mngt"])
    def test_mngt_call(self):
        """test correct call"""
        cli.cli_start.CliStart()
        cli.cli_start.com_mngt.Mngt.assert_called_with(False)

    # ===== - analyse - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "analyse"])
    def test_analyse_call(self):
        """test correct call"""
        cli.cli_start.CliStart()
        cli.cli_start.com_analyse.Analyse.assert_called_with(False)

    # ===== - storage - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "storage"])
    def test_storage_call(self):
        """test correct call"""
        cli.cli_start.CliStart()
        cli.cli_start.com_storage.Storage.assert_called_with(False)

    # ===== - list_habits - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "--demo", "storage"])
    def test_list_habits_call_demo(self):
        """test correct call"""
        cli.cli_start.CliStart().list_habits()
        cli.cli_start.habtrack.storage.deserialize.assert_called_with(file_source="sample")

    # ===== - demo_default - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "storage"])
    def test_demo_default_write_call(self):
        """test correct call"""
        with patch("builtins.open") as patch_open:
            cli.cli_start.CliStart().demo_default()
        patch_open.assert_called()

    # ===== - man - ===== #
    @patch.object(cli.cli_start.sys, "argv", ["", "storage"])
    def test_man_print(self):
        """test correct print input"""
        with patch("builtins.print") as patch_print:
            cli.cli_start.CliStart().man()
        patch_print.assert_called_with("man")

    @classmethod
    def tearDownClass(cls):
        """teardown the mocks"""
        cli.cli_start.sys = TestCliStart.orig_sys
        cli.cli_start.com_analyse = TestCliStart.orig_analyse
        cli.cli_start.com_storage = TestCliStart.orig_storage
        cli.cli_start.com_mngt = TestCliStart.orig_mngt
        cli.cli_start.cli_data = TestCliStart.orig_data
        cli.cli_start.habtrack = TestCliStart.orig_habtrack