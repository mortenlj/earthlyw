from ibidem.earthlyw.identify import find_binary_name

VALID_BINARIES = {
    "earthly-darwin-amd64",
    "earthly-darwin-arm64",
    "earthly-linux-amd64",
    "earthly-linux-arm64",
    "earthly-linux-arm7",
    "earthly-windows-amd64.exe",
}


def test_binary_name():
    actual = find_binary_name()
    assert actual in VALID_BINARIES
