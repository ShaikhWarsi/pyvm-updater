# Quick Start Guide - Python Version Manager (pyvm)

## 🚀 Installation

### Windows Users
1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```cmd
   cd C:\path\to\sideProjects
   ```
3. Run the installer:
   ```cmd
   install.bat
   ```

### Linux/macOS Users
1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/sideProjects
   ```
3. Run the installer:
   ```bash
   ./install.sh
   ```

Or install directly:
```bash
pip install -e .
```

## 📋 Usage Examples

### Check Your Python Version
```bash
pyvm
# or
pyvm check
```

### Update Python to Latest Version
```bash
pyvm update
```

### Update to a Specific Version
```bash
pyvm update --version 3.11.5
```

### Update Without Confirmation (Auto Mode)
```bash
pyvm update --auto
pyvm update --version 3.11.5 --auto
```

### Show System Information
```bash
pyvm info
```

### Show Help
```bash
pyvm --help
```

## 🔧 Troubleshooting

### Command not found: pyvm
The installation directory is not in your PATH. Try:

**Linux/macOS:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc
```

**Windows:**
- The Python Scripts directory should be in PATH
- Usually: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts`
- Or use: `python -m python_version` instead

### Permission Denied (Linux/macOS)
For updates, you may need sudo:
```bash
sudo pyvm update
```

### Missing Dependencies
Install manually:
```bash
pip install requests beautifulsoup4 packaging click
```

## 🌍 Platform Notes

### Windows
- Downloads official .exe installer
- Runs installer GUI
- May require administrator privileges
- **Tip:** Check "Add Python to PATH" during installation

### Linux (Ubuntu/Debian)
- Uses apt package manager
- Requires sudo for system-wide installation
- Uses deadsnakes PPA for latest versions

### Linux (Fedora/RHEL)
- Uses dnf or yum package manager
- Requires sudo privileges

### macOS
- Uses Homebrew if available
- Otherwise provides download link
- Can also use official .pkg installer

## 📝 Example Session

```bash
$ pyvm
Checking Python version... (Current: 3.12.3)

========================================
     Python Version Check Report
========================================
Your version:   3.12.3
Latest version: 3.14.0
========================================
⚠ A new version (3.14.0) is available!

💡 Tip: Run 'pyvm update' to upgrade Python

$ pyvm update
🔍 Checking for updates...

📊 Current version: 3.12.3
📊 Latest version:  3.14.0

🚀 Update available: 3.12.3 → 3.14.0

Do you want to proceed with the update? [y/N]: y

🖥️  Detected: Linux (amd64)
🐧 Linux detected
Using apt package manager...
...
✅ Update process completed!
```

## ✨ Features

✅ Cross-platform (Windows, Linux, macOS)
✅ Automatic version detection
✅ One-command updates
✅ Progress indication
✅ Detailed error messages
✅ Safe with confirmation prompts
✅ Admin privilege detection
✅ Exit codes for scripting

## 🔗 Useful Links

- Python Official: https://www.python.org/downloads/
- pyenv (Alternative): https://github.com/pyenv/pyenv
- Homebrew (macOS): https://brew.sh/

## 💡 Tips

1. **Always backup** important Python projects before major updates
2. **Virtual environments** are not affected by system Python updates
3. **Check compatibility** of your projects before updating
4. **Restart** your terminal/IDE after updates
5. Use **pyenv** or **conda** for managing multiple Python versions

## 🐛 Known Limitations

- Cannot update Python being used to run pyvm itself
- System Python on some Linux distros is protected
- May require manual intervention on some systems
- Update process varies by platform

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify your internet connection
3. Ensure you have proper permissions
4. Check python.org is accessible
5. Try manual installation from python.org

---

**Happy Pythoning! 🐍**
