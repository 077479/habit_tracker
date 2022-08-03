# ========== - package import access - ========== #
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))


# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli, habtrack

# ========== - logic - ========== #
@patch.object(sys, 'argv', ["", "", "__str__"])
def test_class_type():
    assert type(cli.com_storage.Storage(False)) == cli.com_storage.Storage

@patch.object(sys, 'argv', ["", "", "__str__", "-n", "test"])
@patch.object(habtrack.storage, "serialize")
def test_serialize(fake_storage):
    hab = Mock()
    hab.name = "test"
    with patch.object(habtrack.storage, "deserialize", return_value=[hab]):
        cli.com_storage.Storage(False).serialize()    
    fake_storage.assert_called_once()