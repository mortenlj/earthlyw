import pytest
from unittest.mock import patch

from ibidem.earthlyw import identify


class TestIdentify:
    @pytest.mark.parametrize("os, arch, binary_name", (
            ("windows", "x86_64", "earthly-windows-amd64.exe"),
            ("Linux", "x86_64", "earthly-linux-amd64"),
    ))
    def test_binary_name(self, os, arch, binary_name):
        with patch("ibidem.earthlyw.identify.platform.system") as system_mock:
            with patch("ibidem.earthlyw.identify.platform.machine") as machine_mock:
                system_mock.return_value = os
                machine_mock.return_value = arch
                actual = identify.find_binary_name()
                assert actual == binary_name
