# Configuration and constants for pyvm_updater
"""Constants and configuration for pyvm_updater."""

from pathlib import Path

# Network configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
DOWNLOAD_TIMEOUT = 120  # seconds
REQUEST_TIMEOUT = 15  # seconds

# History file location
HISTORY_FILE = Path.home() / ".pyvm_history.json"
