"""Unit tests for __version__.py."""

import diffpy.saf  # noqa


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(diffpy.saf, "__version__")
    assert diffpy.saf.__version__ != "0.0.0"
