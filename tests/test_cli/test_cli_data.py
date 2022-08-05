# ========== - import - ========== #
import pytest, cli

# ========== - logic - ========== #
# ===== - sample - ===== #
def test_sample():
    """test for the type"""
    assert type(cli.cli_data.sample) == str

# ===== - man - ===== #
def test_man():
    """test for the type"""
    assert type(cli.cli_data.man) == list

def test_info_command():
    """test for the type"""
    assert type(cli.cli_data.info_command) == str

def test_mngt():
    """test for the type"""
    assert type(cli.cli_data.info_mngt) == str

def test_analyse():
    """test for the type"""
    assert type(cli.cli_data.info_analyse) == str

def test_storage():
    """test for the type"""
    assert type(cli.cli_data.info_storage) == str

def test_reference():
    """test for the type"""
    assert type(cli.cli_data.reference) == str