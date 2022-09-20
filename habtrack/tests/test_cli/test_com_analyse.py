"""
module test_com_analyse: the test module for the module cli.com_analyse

===== Imports =====
built-in:
    unittest.mock.patch
    unittest.mock.Mock
    unittest
package-intern:
    cli

===== Classes =====
TestAnalyse(unittest.TestCase):
    the test class for the module cli.com_analyse
"""
# ========== - import - ========== #
import unittest, cli#cli.com_analyse
from unittest.mock import Mock, patch

# ========== - logic - ========== #
# ===== init ===== #
class TestAnalyse(unittest.TestCase):

    # ===== setup / teardown ===== #
    @classmethod
    def setUpClass(cls):
        """setup the test environment"""
        cls.fake_hab = Mock()
        cls.fake_hab.name = "fake_hab"

        cls.orig_analys = cli.com_analyse.analyse        
        
        cls.orig_sys = cli.command.sys
        cls.orig_src_storage = cli.command.src.storage

        cli.command.sys = Mock()
        cli.command.sys.argv = ["", "", "__str__", "-n=fake_hab", "-p=weekly"]

        cli.command.src.storage = Mock()
        cli.command.src.storage.deserialize.return_value = [TestAnalyse.fake_hab]


        cli.com_analyse.analyse = Mock()        
        cli.com_analyse.analyse.get_streaks.return_value = list()
        cli.com_analyse.analyse.get_longest_streak.return_value = "test_streak"
        cli.com_analyse.analyse.get_habits_by_period.return_value = "by_period"
        cli.com_analyse.analyse.list_habits.return_value = "list_habs"
        cli.com_analyse.analyse.is_broken.return_value = "is_broken"
        cli.com_analyse.analyse.get_longest_streak_of_habits.return_value = ("hab_name", "longest_of_all")
        cli.com_analyse.analyse.list_checkoffs.return_value = "list_checkoffs"

    @classmethod
    def tearDownClass(cls):
        """teardown the mocks"""
        cli.com_analyse.analyse = TestAnalyse.orig_analys
        cli.command.sys = TestAnalyse.orig_sys
        cli.command.src.storage = TestAnalyse.orig_src_storage        

    # ===== init ===== #
    def test_class_init_type(self):
        """test if the class is instantiable without error"""
        type(cli.com_analyse.Analyse(False)) == cli.com_analyse.Analyse


    # ===== get_streaks ===== #
    def test_get_streaks(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).get_streaks()
        assert cli.com_analyse.analyse.get_streaks.called


    # ===== longest_streak ===== #
    def test_get_longest_streak_print(self):
        """test for the right amount of prints"""
        with patch("builtins.print") as patch_print:
            cli.com_analyse.Analyse(False).get_longest_streak()
        assert patch_print.call_count == 3


    # ===== by period ===== #
    def test_get_habits_by_period_call(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).get_habits_by_period()
        cli.com_analyse.analyse.get_habits_by_period.assert_called_with([TestAnalyse.fake_hab], "weekly")

    def test_get_habits_by_period_print(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).get_habits_by_period()
        cli.com_analyse.analyse.list_habits.assert_called_with("by_period")


    # ===== broken ===== #
    def test_is_broken_call(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).is_broken()
        cli.com_analyse.analyse.is_broken.assert_called_with(TestAnalyse.fake_hab)


    # ===== longest_streak_all ===== #
    def test_get_longest_streak_all_call(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).get_longest_streak_of_habits()
        cli.com_analyse.analyse.get_longest_streak_of_habits.assert_called_with([TestAnalyse.fake_hab])

    # ===== list_checkoffs ===== #
    def test_list_checkoffs_call(self):
        """test for the right call"""
        cli.com_analyse.Analyse(False).list_checkoffs()
        cli.com_analyse.analyse.list_checkoffs.assert_called_with(TestAnalyse.fake_hab)


    # ===== list_habits_call ===== #
    def test_list_habits_call(self):
        """test for the right print call"""
        with patch("builtins.print") as patch_print:
            cli.com_analyse.Analyse(False).list_habits()
        patch_print.assert_called()