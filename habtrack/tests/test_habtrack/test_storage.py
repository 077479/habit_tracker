"""
module test_storage:
    the test module for the storage-functionality

===== Imports =====
built-in:
    datetime
    unittest
    pathlib
package-intern:
    habtrack
    conftest

===== classes =====
TestStorage(unittest.TestCase):
    the actual test class
"""
# ========== - import - ========== #
import unittest, datetime, pathlib
import src
from tests import conftest


# ========== - logic - ========== #
class TestStorage(unittest.TestCase):

    # ===== - Setup / Teardown - ===== #
    @classmethod
    def setUpClass(cls):
        conftest.backup_storage()
        conftest.create_samples()
           
    def setUp(self):
        self.habit_obj = conftest.habit_obj()
        self.sample_habs = conftest.sample_habs()

    def tearDown(self):
        conftest.clean_habit_storage()

    @classmethod
    def tearDownClass(cls):
        conftest.roll_back_storage()


    # ===== - _serialize_habit test - ===== #
    def test__serialize_habit_type(self):
        """test for the right instance"""
        assert isinstance(src.storage._serialize_habit(self.habit_obj), dict)

    def test__serialize_habit_dct_name(self):
        """test for the right state after call"""
        assert src.storage._serialize_habit(self.habit_obj)["name"] == "test_habit"

    def test__serialize_habit_dct_period(self):
        """test for the right state after call"""
        assert src.storage._serialize_habit(self.habit_obj)["periodicity"] == "monthly"

    def test__serialize_habit_dct_desc(self):
        """test for the right state after call"""
        assert src.storage._serialize_habit(self.habit_obj)["description"] == "just here to test the modul"

    def test__serialize_habit_dct_creation_date(self):
        """test for the right state after call"""
        assert src.storage._serialize_habit(self.habit_obj)["creation_date"] == datetime.date(2000,1,1).toordinal()

    def test__serialize_habit_dct_checkoffs(self):
        """test for the right state after call"""
        self.habit_obj.checkoffs.append(datetime.date.fromordinal(730120)) # 2000,1,1
        self.habit_obj.checkoffs.append(datetime.date.fromordinal(730151)) # 2000,2,1
        self.habit_obj.checkoffs.append(datetime.date.fromordinal(730180)) # 2000,3,1
        self.habit_obj.checkoffs.append(datetime.date.fromordinal(730211)) # 2000,4,1
        assert src.storage._serialize_habit(self.habit_obj)["checkoffs"] == [730120, 730151, 730180, 730211]



    # ===== - serialize test - ===== #
    def test_serialize_single_file_creation(self):
        """test for the right state after call"""
        src.storage.serialize(self.habit_obj)
        assert (pathlib.Path(__file__).parents[2] / "data/test_habit.json").exists()

    def test_serialize_single_file_content(self):
        """test for the right state of file after call"""

        test_lines=['{\n',
        '  "_HABIT": true,\n',
        '  "name": "test_habit",\n',
        '  "description": "just here to test the modul",\n',
        '  "periodicity": "monthly",\n',
        '  "amount": 1,\n',
        '  "creation_date": 730120,\n',
        '  "checkoffs": []\n',
        '}']

        src.storage.serialize(self.habit_obj)
        
        with open (pathlib.Path(__file__).parents[2] / "data/test_habit.json", "r") as file:
            file_lines = file.readlines()

        for i in range(len(file_lines)):
            assert file_lines == test_lines

    def test_serialize_collection_file_creation(self):
        """test for the right state of file after call"""
        src.storage.serialize([self.habit_obj])
        assert (pathlib.Path(__file__).parents[2] / "data/habtrack.json").exists()

    def test_serialize_collection_file_content(self):
        """test for the right state of file after call"""
        test_lines=['[\n',
        '  {\n',
        '    "_HABIT": true,\n',
        '    "name": "test_habit",\n',
        '    "description": "just here to test the modul",\n',
        '    "periodicity": "monthly",\n',
        '    "amount": 1,\n',
        '    "creation_date": 730120,\n',
        '    "checkoffs": []\n',
        '  }\n',
        ']']

        src.storage.serialize([self.habit_obj])

        with open (pathlib.Path(__file__).parents[2] / "data/habtrack.json", "r") as file:
            file_lines = file.readlines()

        for i in range(len(file_lines)):
            assert file_lines == test_lines


    # ===== - _deserialize test - ===== #
    def test__deserialize(self):
        """test for the right state after call"""
        hab = src.storage._deserialize_habit({
            "_HABIT": True,
            "name": "test_habit",
            "description": "just here to test the modul",
            "periodicity": "monthly",
            "amount": 1,
            "creation_date": 730120,
            "checkoffs": []
            })
        assert hab == self.habit_obj


    # ===== - deserialize test - ===== #
    def test_deserialize_smoke(self):
        """test if it turns on without exception"""
        src.storage.deserialize()

    def test_deserialize_type(self):
        """test for the right instance"""
        assert isinstance(src.storage.deserialize(), list)

    def test_deserialize_demo_type(self):
        """test for the right attribute"""
        assert src.storage.deserialize(demo=True)[0].__module__ == "src.habit"

    def test_deserialize_demo_len(self):
        """test for the right attribute"""
        assert len(src.storage.deserialize(demo=True)) == 6

    def test_deserialize_file_source_len(self):
        """test for the right length of return"""
        src.storage.serialize([self.habit_obj])
        assert len(src.storage.deserialize(file_source="habit_obj")) == 1

    def test_deserialize_file_source_name(self):
        """test for the right attribute"""
        src.storage.serialize([self.habit_obj])
        assert src.storage.deserialize(file_source="habit_obj")[0].name == "test_habit"