import pytest

from ibidem.earthlyw.identify import find_binary_name


@pytest.fixture()
def binary_name(pytestconfig):
    binary_name = pytestconfig.getoption("binary_name")
    if binary_name is None:
        pytest.fail("Binary name not set")
    return binary_name


def test_binary_name(binary_name):
    actual = find_binary_name()
    assert binary_name == actual
