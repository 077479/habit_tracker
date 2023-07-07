"""
module test_habit:
    the test module for the habit-obj

===== Imports =====
built-in:
    datetime
    pytest
    unittest
    parameterized
package-intern:
    conftest
    habtrack

===== classes =====
TestHabit(unittest.TestCase):
    the actual test class
"""
# ========== - import - ========== #
import unittest, pytest, datetime, parameterized
from tests import conftest
import src


# ========== - logic - ========== #
class TestHabit(unittest.TestCase):

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


    # ===== - init - ===== #
    def test_habit_init_name(self):
        """test for correct attribute after creation"""
        assert self.habit_obj.name == "test_habit"
    def test_habit_init_desc(self):
        """test for correct attribute after creation"""
        assert self.habit_obj.description == "just here to test the modul"
    def test_habit_init_periodicity(self):
        """test for correct attribute after creation"""
        assert self.habit_obj.periodicity(datetime.date(2000,1,1), 1) == (datetime.date(2000,1,1), datetime.date(2000,2,1))

    @parameterized.parameterized.expand([("none", None), ("str","gibberish"), ("int", 13)])
    def test_habit_defect_parameters(self, name, periods):
        """test for the correct exception called"""
        with pytest.raises(TypeError):
            src.habit.Habit("name", periods)


    # ===== - check_off test - ===== #
    def test_habit_check_off_created(self):
        """test for correct call"""
        self.habit_obj.check_off()
        assert self.habit_obj.checkoffs[0] == datetime.date.today()

    def test_habit_check_off_amount(self):
        """test for correct amount after certain calls"""
        for i in range(5):
            self.habit_obj.check_off()
        assert len(self.habit_obj.checkoffs) == 5


    # ===== - __str__ test - ===== #
    def test_set_periodicity(self):
        """test for correct return"""
        self.habit_obj.set_periodicity("daily")
        assert self.habit_obj.periodicity(datetime.date(2000,1,1), 1) == (datetime.date(2000,1,1), datetime.date(2000,1,2))


    # ===== - __str__ test - ===== #
    def test_habit_str_repr(self):
        """test for correct return"""
        assert str(self.habit_obj) == f"Habit: test_habit | {str(datetime.date(2000,1,1))} | monthly | amount: 1"


    # ===== - __eq__ test - ===== #
    def test_habit_equality(self):
        """test for correct return"""
        hab = src.habit.Habit(name="test_habit", periodicity="monthly", description="just here to test the modul")
        hab.creation_date = datetime.date(2000,1,1)
        assert self.habit_obj == hab

    
    @parameterized.parameterized.expand([("hab_1", src.habit.Habit("test", "monthly")),
                                        ("int", 238),
                                        ("hab_2", src.habit.Habit("john", "weekly")),
                                        ("str", "hmmw")])
    @unittest.expectedFailure
    def test_habit_equality_defect(self, name, defect):
        """test for correct behavior for defect input"""
        if "int" == name == "str" in name:
            with pytest.raises(AttributeError):
                assert self.habit_obj == defect
        else:
            assert self.habit_obj == defect

