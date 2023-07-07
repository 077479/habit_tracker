"""
module test_manual: the test module for the module manual

===== Imports =====
built-in:
    unittest.mock.patch
    unittest.mock.Mock
    unittest
    time
package-intern:
    cli

===== Classes =====
TestManual(unittest.TestCase):
    the test class for the module manual
"""
# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli, unittest, time


# ========== - logic - ========== #
class TestManual(unittest.TestCase):
    
    # ===== - setup / teardown - ===== #
    @classmethod
    def setUpClass(cls):
        """setup the test environment"""

        cls.orig_subprocess = cli.manual.subprocess
        cls.orig_time = cli.manual.time
        cls.orig_data = cli.manual.cli.cli_data
        
        cli.manual.subprocess = Mock()
        cli.manual.subprocess.run.return_value = None
        cli.manual.cli.cli_data = Mock()
        cli.manual.cli.cli_data.man = [1,2,3]

    @classmethod
    def tearDownClass(cls):
        """reset the mocks to origin"""
        cli.manual.subprocess = TestManual.orig_subprocess
        cli.manual.time = TestManual.orig_time 
        cli.manual.cli.cli_data = TestManual.orig_data  


    # ===== - wait_key - ===== #
    def test_wait_key_windows(self):
        """test for the right call if platform is windows"""
        
        with patch.object(cli.manual.platform, "system", return_value="windows"):
            cli.manual.wait_key()
        cli.manual.subprocess.run.assert_called_with("pause", shell=True)

    def test_wait_key_linux(self):
        """test for the right call if platform is linux"""
        with patch.object(cli.manual.platform, "system", return_value="linux"):
            cli.manual.wait_key()
        cli.manual.subprocess.run.assert_called_with('read -p "press enter to continue ..."', shell=True)


    # ===== - print slow - ===== #
    def test_print_slow_time(self):
        """test if the process was frozen for given time"""
        start = time.time()
        with patch("cli.manual.time.sleep") as patch_time:
            cli.manual.print_slow("", 15)
        end = time.time()
        assert int(end-start) < 15


    # ===== - run_shell - ===== #
    def test_run_shell_time(self):
        """test if the process was frozen for given time"""
        start = time.time()
        with patch("cli.manual.time") as patch_time:
            cli.manual.run_shell("", 746)
        end = time.time()
        assert int(end-start) < 746

    def test_run_shell_subp(self):
        """test for the right call"""
        cli.manual.run_shell("", 746)
        cli.manual.subprocess.run.assert_called_with("", shell=True)


    # ===== - man_gen - ===== #
    def test_man_gen(self):
        """test if the return is correct"""
        gen = cli.manual.man_gen()
        ret_val = [i for i in gen]
        assert ret_val == [1,2,3]