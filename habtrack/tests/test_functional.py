# ========== - import - ========== #
import unittest, pathlib, subprocess
from tests import conftest

# ========== - logic - ========== #
class Test_EtwoE(unittest.TestCase):

    # ===== - Setup / Teardown - ===== #
    @classmethod
    def setUpClass(cls):
        conftest.backup_storage()
        conftest.create_samples()

        cls.work_dir = str(pathlib.Path(__file__).parents[1])
    
    def setUp(self):
        conftest.create_samples()

    @classmethod
    def tearDownClass(cls):
        conftest.roll_back_storage()
        

    # ===== - mngt - ===== #
    def test_mngt_create(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo mngt create -n=test_software -p=daily -d="test at leasttwice a day" -a=2'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_mngt_check_off(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo mngt check_off -n=work'
        result =subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_mngt_change_period(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo mngt change_period -n=work -p=weekly -a=14'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_mngt_delete(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo mngt delete_habit -n=work'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0
    
    
    # ===== - analyse - ===== #
    def test_get_habits_by_period(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse get_habits_by_period -p=weekly'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_get_longest_streak(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse get_longest_streak -n=work'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_get_longest_streak_of_habits(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse get_longest_streak_of_habits'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_get_streaks(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse get_streaks -n=vacuum_clean'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_is_broken(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse is_broken -n=vacuum_clean'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_list_checkoffs(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse list_checkoffs -n=vacuum_clean'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0    

    def test_list_habits(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo analyse list_habits'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0


    # ===== - storage - ===== #
    def test_serialize(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo storage serialize -n=vacuum_clean'
        result = subprocess.run(command, shell=True)

        if (pathlib.Path(__file__).parents[1] / "data/vacuum_clean.json").exists():
            (pathlib.Path(__file__).parents[1] / "data/vacuum_clean.json").unlink()

        assert result.returncode == 0
    

    # ===== - commands - ===== #
    def test_list_habits(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py --demo list_habits'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0

    def test_reference(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py reference'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0

    def test_demo_default(self):
        command = f'python {Test_EtwoE.work_dir}/habtrack.py demo_default'
        result = subprocess.run(command, shell=True)
        assert result.returncode == 0