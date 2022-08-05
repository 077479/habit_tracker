# ========== - import - ========== #
import pytest, cli

# ========== - logic - ========== #
# ===== - sample - ===== #
def test_sample():
    """test for the type"""
    assert type(cli.cli_data.sample) == str

# ===== - man - ===== #
def test_man():
    """test for teh type"""
    assert type(cli.cli_data.man) == str