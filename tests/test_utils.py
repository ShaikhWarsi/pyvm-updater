"""Tests for pyvm_updater.utils module."""


from pyvm_updater.utils import get_os_info, validate_version_string


class TestValidateVersionString:
    """Tests for validate_version_string function."""

    def test_valid_major_minor_patch(self):
        """Test valid X.Y.Z format."""
        assert validate_version_string("3.11.5") is True
        assert validate_version_string("3.12.1") is True
        assert validate_version_string("2.7.18") is True

    def test_valid_major_minor(self):
        """Test valid X.Y format."""
        assert validate_version_string("3.11") is True
        assert validate_version_string("3.9") is True

    def test_valid_extended_version(self):
        """Test valid X.Y.Z.A format."""
        assert validate_version_string("3.11.5.1") is True

    def test_invalid_empty_string(self):
        """Test empty string returns False."""
        assert validate_version_string("") is False

    def test_invalid_single_number(self):
        """Test single number is invalid."""
        assert validate_version_string("3") is False

    def test_invalid_text(self):
        """Test text strings are invalid."""
        assert validate_version_string("latest") is False
        assert validate_version_string("stable") is False

    def test_invalid_with_letters(self):
        """Test versions with letters are invalid."""
        assert validate_version_string("3.11.5a") is False
        assert validate_version_string("3.11rc1") is False

    def test_invalid_with_special_chars(self):
        """Test versions with special characters are invalid."""
        assert validate_version_string("3.11-5") is False
        assert validate_version_string("3.11_5") is False


class TestGetOsInfo:
    """Tests for get_os_info function."""

    def test_returns_tuple(self):
        """Test that get_os_info returns a tuple."""
        result = get_os_info()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_os_name_is_lowercase(self):
        """Test that OS name is lowercase."""
        os_name, _ = get_os_info()
        assert os_name == os_name.lower()

    def test_arch_is_normalized(self):
        """Test that architecture is normalized to amd64, arm64, or x86."""
        _, arch = get_os_info()
        assert arch in ["amd64", "arm64", "x86"]
