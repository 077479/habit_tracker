# ========== - import - ========== #
from unittest.mock import patch, Mock
import cli



# ========== - logic - ========== #
orig_argv = cli.command.sys.argv
fake_argv = ["", "", "__str__", "-n=test"]
fake_hab = Mock()
fake_hab.name = "test"

# ===== init ===== #
def test_class_init_type():
    """test for correct initialization"""
    with patch.object(cli.command.sys, "argv", fake_argv):
        assert type(cli.com_storage.Storage(False)) == cli.com_storage.Storage

# ===== serialize ===== #
@patch.object(cli.command.habtrack.storage, "deserialize", return_value=[fake_hab])
@patch.object(cli.com_storage.habtrack.storage, "serialize")
def test_serialize_call(patch_se, patch_de):
    """test for correct call"""
    with patch.object(cli.command.sys, "argv", fake_argv):
        cli.com_storage.Storage(False).serialize()
    patch_se.called_with(fake_hab)