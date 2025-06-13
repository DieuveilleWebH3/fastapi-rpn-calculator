import os
import json
import tempfile
import pytest
from unittest import mock
from app.fixtures import load_fixtures

from typing import Iterator

@pytest.fixture
def temp_seed_file() -> Iterator[str]:
    """Create a temporary JSON file with seed data."""
    data: list[dict[str, float | str]] = [
        {"id": 1, "expression": "2 3 +", "result": 5.0},
        {"id": 2, "expression": "3 4 *", "result": 12.0}
    ]
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tf:
        json.dump(data, tf)
        tf.flush()
        yield tf.name
    os.remove(tf.name)

def test_load_seed_data_success(temp_seed_file: str):
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        load_fixtures.load_seed_data(temp_seed_file)
        assert mock_session.merge.call_count == 2
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

def test_load_seed_data_file_not_found():
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        with mock.patch("logging.error") as mock_log:
            load_fixtures.load_seed_data("nonexistent.json")
            mock_log.assert_any_call("File not found: nonexistent.json")

def test_load_seed_data_permission_error(temp_seed_file: str):
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        with mock.patch("builtins.open", side_effect=PermissionError):
            with mock.patch("logging.error") as mock_log:
                load_fixtures.load_seed_data(temp_seed_file)
                mock_log.assert_any_call(f"Permission denied when accessing the file '{temp_seed_file}'.")

def test_load_seed_data_json_decode_error(temp_seed_file: str):
    # Overwrite file with invalid JSON
    with open(temp_seed_file, "w") as f:
        f.write("{ invalid json }")
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        with mock.patch("logging.error") as mock_log:
            load_fixtures.load_seed_data(temp_seed_file)
            assert any("Failed to parse JSON" in call.args[0] for call in mock_log.call_args_list)

def test_load_seed_data_unexpected_exception(temp_seed_file: str):
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_session.merge.side_effect = RuntimeError("Unexpected error")
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        with mock.patch("logging.error") as mock_log:
            load_fixtures.load_seed_data(temp_seed_file)
            assert any("An unexpected error occurred" in call.args[0] for call in mock_log.call_args_list)
def test_load_seed_data_logs_info(temp_seed_file: str):
    with mock.patch("app.fixtures.load_fixtures.get_engine_and_session") as mock_get_engine_and_session:
        mock_session = mock.MagicMock()
        mock_get_engine_and_session.return_value = (None, lambda: mock_session)
        with mock.patch("logging.info") as mock_info_log:
            load_fixtures.load_seed_data(temp_seed_file)
            mock_info_log.assert_any_call("Seed data loaded.")
