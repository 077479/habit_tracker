"""
module test_period:
    the test module for the period-obj

===== Imports =====
built-in:
    datetime
    pytest
    unittest
3rd_party:
    parameterized.parameterized
package-intern:
    habtrack

===== classes =====
TestPeriod(unittest.TestCase):
    the actual test class
"""
# ========== - import - ========== #
from parameterized import parameterized
import unittest, pytest, datetime
import src

# ========== - logic - ========== #
class TestPeriod(unittest.TestCase):

    # ===== - init - ===== #
    def test_period_init_1(self):
        """test for the right state after initialization"""
        assert src.period.Period("daily").period == "daily"
    def test_period_init_2(self):
        """test for the right state after initialization"""
        assert src.period.Period("daily").period == "daily"
    def test_period_init_3(self):
        """test for the right state after initialization"""
        assert src.period.Period("daily").period == "daily"

    @parameterized.expand([("none", None), ("int", 1), ("str", "gibberish")])
    def test_period_init_defect_input(self, name, periodicity):
        """test for the right exception after defect input"""
        with pytest.raises(TypeError):
            src.period.Period(periodicity)


    # # ===== - object - ===== #
    def test_period_set_fct_1(self):
        """test for the right state after initialization"""
        src.period.Period("daily")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,1,2))
    def test_period_set_fct_2(self):
        """test for the right state after initialization"""
        src.period.Period("daily")(datetime.date(2000,1,1),4) == (datetime.date(2000,1,1), datetime.date(2000,1,5))
    def test_period_set_fct_3(self):
        """test for the right state after initialization"""
        src.period.Period("weekly")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,1,8))
    def test_period_set_fct_4(self):
        """test for the right state after initialization"""
        src.period.Period("monthly")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,2,1))