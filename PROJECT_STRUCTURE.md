# Project Structure

This document describes the organization of the pyvm-updater codebase.

```
pyvm-updater/
├── pyproject.toml              # Package configuration and dependencies
├── README.md                   # Main documentation
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
│
├── src/pyvm_updater/           # Main package (Python source)
│   ├── __init__.py             # Package metadata and version
│   ├── cli.py                  # CLI commands (click)
│   ├── config.py               # Configuration management
│   ├── constants.py            # Global constants
│   ├── history.py              # Installation history tracking
│   ├── installers.py           # Platform specific installers
│   ├── logging_config.py       # Logging configuration
│   ├── tui.py                  # Terminal User Interface (textual)
│   ├── utils.py                # Utility functions
│   ├── venv.py                 # Virtual environment management
│   └── version.py              # Version checking and fetching
│
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_history.py         # Tests for history module
│   ├── test_utils.py           # Tests for utils module
│   ├── test_venv.py            # Tests for venv module
│   └── test_version.py         # Tests for version module
│
├── docs/                       # Documentation
│   ├── CRITICAL_SECURITY_FIX_v1.2.1.md
│   ├── FIXES_SUMMARY.md
│   ├── INSTALL.md
│   ├── QUICK_REFERENCE.md
│   └── QUICKSTART.md
│
├── install.sh                  # Linux/macOS installation script
├── install.bat                 # Windows installation script
└── check_requirements.py       # Pre installation verification
```

## Module Descriptions

### Core Package (src/pyvm_updater/)

| Module | Description |
|--------|-------------|
| `cli.py` | Command line interface using Click framework |
| `config.py` | Configuration file management (~/.config/pyvm/config.toml) |
| `constants.py` | Network timeouts, file paths, and other constants |
| `history.py` | Tracks installation/update history for rollback support |
| `installers.py` | Platform specific Python installation logic |
| `logging_config.py` | Configurable logging with verbose/quiet modes |
| `tui.py` | Interactive Terminal User Interface using Textual |
| `utils.py` | Helper functions for downloads, checksums, and validation |
| `venv.py` | Virtual environment creation and management |
| `version.py` | Version checking against python.org |

### Test Suite (tests/)

All tests use pytest. Run with:
```bash
pytest tests/ -v
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `pyvm check` | Check current Python version against latest |
| `pyvm list` | List available Python versions |
| `pyvm install <version>` | Install a specific Python version |
| `pyvm update` | Update to the latest Python version |
| `pyvm remove <version>` | Remove an installed Python version |
| `pyvm rollback` | Undo the last installation |
| `pyvm config` | View or manage configuration |
| `pyvm venv create <name>` | Create a virtual environment |
| `pyvm venv list` | List virtual environments |
| `pyvm venv remove <name>` | Remove a virtual environment |
| `pyvm tui` | Launch interactive TUI |
| `pyvm info` | Show system information |

## Configuration

Configuration is stored at `~/.config/pyvm/config.toml`:

```toml
[general]
auto_confirm = false
verbose = false
preferred_installer = "auto"

[download]
verify_checksum = true
max_retries = 3
timeout = 120

[tui]
theme = "dark"
```

## Development

Install in development mode:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest tests/ -v
```

### Dependencies

**Runtime:**
- requests
- beautifulsoup4
- packaging
- click
- textual (optional, for TUI)

**Development:**
- pytest
- pytest-cov
- mypy
- black
- ruff
