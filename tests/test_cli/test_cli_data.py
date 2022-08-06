"""
module test_cli_data: test file for the cli_data module

===== Imports =====
package-intern:
    cli
"""

# ========== - import - ========== #
import cli

# ========== - logic - ========== #
# ===== - sample - ===== #
def test_sample():
    """
    test_sample:
        test for the type
    """

    assert type(cli.cli_data.sample) == str

# ===== - man - ===== #
def test_man():
    """
    test_man:
        test for the type
    """

    assert type(cli.cli_data.man) == list

def test_info_command():
    """
    test_info_command:
        test for the type
    """
    
    assert type(cli.cli_data.info_command) == str

def test_mngt():
    """
    test_mngt:
        test for the type
    """

    assert type(cli.cli_data.info_mngt) == str

def test_analyse():
    """
    test_analyse:
        test for the type
    """

    assert type(cli.cli_data.info_analyse) == str

def test_storage():
    """
    test_storage:
        test for the type
    """
    
    assert type(cli.cli_data.info_storage) == str

def test_reference():
    """
    test_reference:
        test for the type
    """

    assert type(cli.cli_data.reference) == str