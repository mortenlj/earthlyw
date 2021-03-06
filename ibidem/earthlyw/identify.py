import logging
import platform

LOG = logging.getLogger(__name__)

ARCHS = {
    "x86_64": "amd64",
    "aarch64": "arm64",
}


def find_binary_name():
    """Figure out the name of the binary we're going to need, based on OS and Arch"""
    LOG.debug("Figure out name of binary...")
    ext = ""
    os = platform.system().lower()
    if os == "windows":
        ext = ".exe"
    arch = ARCHS.get(platform.machine(), platform.machine())
    binary_name = "earthly-{}-{}{}".format(os, arch, ext)
    LOG.debug("... %r", binary_name)
    return binary_name


def select_version():
    """Find out which version of earthly we need

    For now, always "latest"
    """
    LOG.debug("Figure out which version of earthly we need...")
    LOG.debug("... 'latest'")
    return "latest"
