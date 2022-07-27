import pathlib, sys, pytest, datetime
sys.path.append(str(pathlib.Path(__file__).parents[1]))
from habtrack import period


##### - TODO outsource to "conftest.py" - #####
@pytest.fixture
def period_obj():
    """returns a period object for test purposes"""
    return period.Period("monthly")

##### - __init__ test         - #####
@pytest.mark.parametrize("periodicity", ["daily", "weekly", "monthly"])
def test_period_obj(periodicity):
    """tests if a Period object is instanciated"""
    assert isinstance(period.Period(periodicity), period.Period)

@pytest.mark.parametrize("periodicity", [None, 1, "gibberish"])
def test_period_obj_defect_input(periodicity):
    """test if defect input for a period object will raise the correct error"""
    with pytest.raises(TypeError):
        period(periodicity)



##### - amount_checkoffs test - #####
def test_period_amount_checkoffs_default(period_obj):
    """test if the default amount of checkoffs is assigned"""
    assert period_obj.amount_checkoffs == 1

def test_period_amount_checkoffs_change(period_obj):
    """test if the amount of checkoffs can be changed"""
    period_obj.amount_checkoffs = 36
    assert period_obj.amount_checkoffs == 36



##### - amount_checkoffs test - #####
@pytest.mark.parametrize("periods, start_date, end_date", [
    ("daily", datetime.date(2000, 1, 1), datetime.date(2000, 1, 2)), 
    ("weekly", datetime.date(2000, 1, 1), datetime.date(2000, 1, 8)),
    ("monthly", datetime.date(2000, 1, 1), datetime.date(2000, 2, 1))])
def test_period_set_fct_daily(periods, start_date, end_date):
    """test functionality is correctly assigned and works intentionally"""
    assert period.Period(periods)(start_date, 1) == end_date