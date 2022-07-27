import pathlib, sys, pytest
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

##### - _set_fct test         - #####

##### - _add_day test         - #####

##### - _add_week test        - #####

##### - _add_month test       - #####

##### - __call__ test         - #####