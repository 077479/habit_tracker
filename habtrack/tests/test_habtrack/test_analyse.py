"""
module test_analyse:
    the test module for the analyse functionality

    relies that habtrack.storage works

===== Imports =====
built-in:
    datetime
    pytest
    unittest
package-intern:
    conftest

===== classes =====
TestAnalyse(unittest.TestCase):
    the actual test class
"""
# ========== - import - ========== #
import datetime, pytest, unittest
from src import analyse
from tests import conftest


# ========== - logic - ========== #
class TestAnalyse(unittest.TestCase):

    # ===== - Setup / Teardown - =====#
    @classmethod
    def setUpClass(cls):
        conftest.backup_storage()
        conftest.create_samples()

        cls.habit_obj = conftest.habit_obj()
        cls.sample_habs = conftest.sample_habs()

    def tearDown(self):
        conftest.clean_habit_storage()
    
    @classmethod
    def tearDownClass(cls):
        conftest.roll_back_storage()

    # ===== - get_streaks - # ===== #
    def test_get_streaks_smoke(self):
        """test if it turns on"""
        analyse.get_longest_streak(TestAnalyse.habit_obj)

    def test_get_streaks_type(self):
        """test for the right type"""
        assert isinstance(analyse.get_streaks(TestAnalyse.habit_obj), list)

    def test_get_streaks_isinstance_element_type(self):
        """test for the right type"""
        assert isinstance(analyse.get_streaks(TestAnalyse.habit_obj)[0], list)

    def test_get_streaks_element_len(self):
        """test for the right length of the return"""
        assert len(analyse.get_streaks(TestAnalyse.sample_habs[0])[0]) == 4

    def test_get_streaks_len(self):
        """test for correct return"""
        # [2,4,3,3,1,1]
        lengths = []
        for i in range(6):
            lengths.append(len(analyse.get_streaks(TestAnalyse.sample_habs[i])))
        assert lengths == [2,4,3,3,1,1]


    # ===== - get_longest_streak - ===== #
    def test_get_longest_streak_1(self):
        """test for correct return"""
        assert analyse.get_longest_streak(TestAnalyse.sample_habs[0]) == [
            datetime.date.fromordinal(730120),
            datetime.date.fromordinal(730121),
            datetime.date.fromordinal(730122),
            datetime.date.fromordinal(730123),
        ]

    def test_get_longest_streak_2(self):
        """test correct return"""
        assert analyse.get_longest_streak(TestAnalyse.sample_habs[3]) == [
            datetime.date.fromordinal(730122),
            datetime.date.fromordinal(730124),
            datetime.date.fromordinal(730126),
            datetime.date.fromordinal(730128),
            datetime.date.fromordinal(730131)
        ]


    # ===== - get_habits_by_period - ===== #
    def test_get_habits_by_period_len_1(self):
        """test for correct length of return"""
        assert len(analyse.get_habits_by_period(TestAnalyse.sample_habs, "weekly")) == 2

    def test_get_habits_by_period_len_2(self):
        """test for correct length of return"""
        assert len(analyse.get_habits_by_period(TestAnalyse.sample_habs, "monthly")) == 2


    # ===== - is_broken - ===== # =====##
    def test_is_broke_1(self):
        """test for correct return"""
        for hab in TestAnalyse.sample_habs:
            assert analyse.is_broken(hab)

    @pytest.mark.xfail
    def test_is_broke_2(self):
        """test for correct return"""
        TestAnalyse.sample_habs[0].check_off()
        assert analyse.is_broken(TestAnalyse.sample_habs[0])


    # ===== - get_longest_streak_of_habits - ===== #
    def test_get_longest_streak_of_habits_type(self):
        """test for correct return type"""
        assert isinstance(analyse.get_longest_streak_of_habits(TestAnalyse.sample_habs), tuple)

    def test_get_longest_streak_of_habits_name(self):
        """test for correct return"""
        assert analyse.get_longest_streak_of_habits(TestAnalyse.sample_habs)[0].name == "pay_rent"

    def test_get_longest_streak_of_habits_len(self):
        """test for correct length of return"""
        assert len(analyse.get_longest_streak_of_habits(TestAnalyse.sample_habs)[1]) == 8


    # # ===== - list_habits - ===== #
    def test_list_habits(self):
        assert "vacuum_clean" in analyse.list_habits(TestAnalyse.sample_habs)


    # ===== - list_checkoffs - ===== #
    def test_list_checkoffs(self):
        """test for correct return type"""
        assert isinstance(analyse.list_checkoffs(TestAnalyse.sample_habs[0]), str)