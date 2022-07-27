import pytest, datetime

@pytest.fixture
def start_date():
    """returns datetime.date(year=2000, month=1, day=1)"""
    return datetime.date(2000,1,1)

@pytest.fixture
def period():
    """returns a period object for testpurposes"""
