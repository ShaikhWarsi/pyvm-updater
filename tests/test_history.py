"""Tests for pyvm_updater.history module."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from pyvm_updater.history import HistoryManager


class TestHistoryManager:
    """Tests for HistoryManager class."""

    @pytest.fixture
    def temp_history_file(self):
        """Create a temporary history file for testing."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("[]")
            temp_path = Path(f.name)
        yield temp_path
        # Cleanup
        if temp_path.exists():
            temp_path.unlink()

    def test_get_history_empty_file(self, temp_history_file):
        """Test get_history with empty file."""
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            result = HistoryManager.get_history()
            assert result == []

    def test_get_history_nonexistent_file(self, temp_history_file):
        """Test get_history with nonexistent file."""
        temp_history_file.unlink()  # Delete the file
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            result = HistoryManager.get_history()
            assert result == []

    def test_save_and_get_history(self, temp_history_file):
        """Test save_history and get_history round-trip."""
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            HistoryManager.save_history("install", "3.12.1")
            history = HistoryManager.get_history()
            assert len(history) == 1
            assert history[0]["action"] == "install"
            assert history[0]["version"] == "3.12.1"

    def test_get_last_action_empty(self, temp_history_file):
        """Test get_last_action with empty history."""
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            result = HistoryManager.get_last_action()
            assert result is None

    def test_get_last_action(self, temp_history_file):
        """Test get_last_action returns most recent entry."""
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            HistoryManager.save_history("install", "3.11.5")
            HistoryManager.save_history("update", "3.12.1")
            result = HistoryManager.get_last_action()
            assert result is not None
            assert result["action"] == "update"
            assert result["version"] == "3.12.1"

    def test_history_limit(self, temp_history_file):
        """Test that history is limited to 10 entries."""
        with patch("pyvm_updater.history.HISTORY_FILE", temp_history_file):
            for i in range(15):
                HistoryManager.save_history("install", f"3.{i}.0")
            history = HistoryManager.get_history()
            assert len(history) == 10
