"""
module test_main:
    the test module for the main module

===== Imports =====
built-in:
    datetime
    pytest
    unittest
package-intern:
    conftest
    habtrack

===== classes =====
TestMain(unittest.TestCase):
    the actual test class
"""
# ========== - import - ========== #
import unittest, pytest, datetime
import src
from tests import conftest


# ========== - logic - ========== #
class TestMain(unittest.TestCase):

    # ===== - Setup / Teardown - ===== #
    @classmethod
    def setUpClass(cls):
        conftest.backup_storage()
        conftest.create_samples()
           
    def setUp(self):
        self.habit_obj = conftest.habit_obj()
        self.sample_habs = conftest.sample_habs()

    def tearDown(self):
        conftest.clean_habit_storage()

    @classmethod
    def tearDownClass(cls):
        conftest.roll_back_storage()
            
    # ===== - create_habit test - ===== #
    def test_create_habit_type(self):
        """test for the correct type"""
        hab = src.main.create_habit(name="NEMO_TEST", periodicity="daily")
        assert hab.__module__ == "src.habit"

    def test_create_habit_name(self):
        """test for correct attribute after creation"""
        hab = src.main.create_habit(name="NEMO_TEST", periodicity="daily")
        assert hab.name == "NEMO_TEST"


    # ===== - delete_habit test - ===== #
    def test_delete_habit_test(self):
        """test for right state after call"""
        habs = self.sample_habs
        
        assert habs[0].name == "work"
        src.main.delete_habit(habs[0], habs)
        with pytest.raises(AttributeError):
            assert habs[0] == "work"


    # ===== - check_off test - ===== #
    def test_check_off_len(self):
        """test for right state after call"""
        src.main.check_off(self.habit_obj)
        assert len(self.habit_obj.checkoffs) == 1

    def test_check_off_date(self):
        """test for right state after call"""
        src.main.check_off(self.habit_obj)
        assert self.habit_obj.checkoffs[0] == datetime.date.today()


    # ===== - change_period test - ===== #
    def test_change_period_type(self):
        """test for right state after call"""
        src.main.change_period(self.habit_obj, "daily")
        assert self.habit_obj.periodicity.__module__ == "src.period"
        
    def test_change_period_name(self):
        """test for right state after call"""
        src.main.change_period(self.habit_obj, "daily")
        assert self.habit_obj.periodicity.period == "daily"