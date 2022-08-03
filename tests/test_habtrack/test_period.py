# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))


# ========== - import - ========== #
from habtrack import period
import pytest, datetime

# ========== - logic - ========== #

# ===== - init - ===== #
def test_period_init_1():
    assert period.Period("daily").period == "daily"
def test_period_init_2():
    assert period.Period("daily").period == "daily"
def test_period_init_3():
    assert period.Period("daily").period == "daily"

@pytest.mark.parametrize("periodicity", [None, 1, "gibberish"])
def test_period_init_defect_input(periodicity):
    with pytest.raises(TypeError):
        period.Period(periodicity)


# # ===== - object - ===== #
def test_period_set_fct_1():
    period.Period("daily")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,1,2))
def test_period_set_fct_2():
    period.Period("daily")(datetime.date(2000,1,1),4) == (datetime.date(2000,1,1), datetime.date(2000,1,5))
def test_period_set_fct_3():
    period.Period("weekly")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,1,8))
def test_period_set_fct_4():
    period.Period("monthly")(datetime.date(2000,1,1),1) == (datetime.date(2000,1,1), datetime.date(2000,2,1))