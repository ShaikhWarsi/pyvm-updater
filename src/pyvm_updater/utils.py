"""Utility functions for pyvm_updater."""

from __future__ import annotations

import hashlib
import os
import platform
import re
import time

import click
import requests

from .constants import DOWNLOAD_TIMEOUT, MAX_RETRIES, REQUEST_TIMEOUT, RETRY_DELAY


def get_os_info() -> tuple[str, str]:
    """Detect the operating system and architecture."""
    os_name = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize architecture names
    if machine in ["amd64", "x86_64"]:
        arch = "amd64"
    elif machine in ["arm64", "aarch64"]:
        arch = "arm64"
    else:
        arch = "x86"

    return os_name, arch


def is_admin() -> bool:
    """Check if script is running with admin/sudo privileges."""
    try:
        if platform.system().lower() == "windows":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0  # type: ignore[attr-defined]
        else:
            return hasattr(os, "geteuid") and os.geteuid() == 0
    except Exception:
        return False


def validate_version_string(version_str: str) -> bool:
    """Validate that version string matches expected format (e.g., 3.11.5)."""
    if not version_str:
        return False
    pattern = r"^\d+\.\d+(\.\d+)*$"
    return bool(re.match(pattern, version_str))


def calculate_sha256(file_path: str) -> str:
    """Calculate SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def fetch_remote_sha256(checksum_url: str) -> str | None:
    """Fetch SHA256 checksum from python.org."""
    try:
        response = requests.get(checksum_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.text.strip().split()[0]
    except Exception as e:
        click.echo(f"❌ Failed to fetch checksum: {e}")
        return None


def verify_file_checksum(file_path: str, checksum_url: str) -> bool:
    """Verify downloaded file against python.org SHA256."""
    click.echo("🔐 Verifying file integrity (SHA256)...")

    expected = fetch_remote_sha256(checksum_url)
    if not expected:
        click.echo("❌ Could not retrieve official checksum")
        return False

    actual = calculate_sha256(file_path)

    if actual.lower() != expected.lower():
        click.echo("❌ Checksum mismatch!")
        click.echo(f"Expected: {expected}")
        click.echo(f"Actual:   {actual}")
        return False

    click.echo("✅ Integrity verified")
    return True


def download_file(url: str, destination: str, max_retries: int = MAX_RETRIES) -> bool:
    """Download a file with retry logic, progress indication, and cleanup."""
    if not url.startswith(("http://", "https://")):
        click.echo(f"❌ Invalid URL: {url}")
        return False

    for attempt in range(max_retries):
        try:
            response = requests.get(url, stream=True, timeout=DOWNLOAD_TIMEOUT)

            if 400 <= response.status_code < 500:
                click.echo(f"❌ Download failed with client error {response.status_code}")
                return False

            response.raise_for_status()

            total_size = int(response.headers.get("content-length", 0))
            chunk_size = 8192

            with (
                open(destination, "wb") as f,
                click.progressbar(
                    length=total_size,
                    label="⬇ Downloading",
                    show_eta=True,
                    show_percent=True,
                ) as bar,
            ):
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))

            if not os.path.exists(destination):
                click.echo("❌ Download failed: file not found")
                return False

            if total_size and os.path.getsize(destination) != total_size:
                click.echo(f"❌ File size mismatch. Expected {total_size}, got {os.path.getsize(destination)}")
                raise OSError("File size mismatch")

            return True

        except (OSError, requests.RequestException) as e:
            if os.path.exists(destination):
                try:
                    os.remove(destination)
                except OSError:
                    pass

            if attempt < max_retries - 1:
                wait_time = RETRY_DELAY * (attempt + 1)
                click.echo(f"\n⚠️ Attempt {attempt + 1} failed: {e}")
                click.echo(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                click.echo(f"\n❌ All download attempts failed: {e}")
                return False

    return False
