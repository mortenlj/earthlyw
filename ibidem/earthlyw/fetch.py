import os
import logging

import appdirs

LOG = logging.getLogger(__name__)


def _download_binary(version, binary_name, binary_path):
    raise NotImplementedError("Not yet implemented")


def provide_binary(version, binary_name):
    app_dir = appdirs.AppDirs("earthlyw", version=version)
    binary_path = os.path.join(app_dir.user_cache_dir, binary_name)
    LOG.debug("See if we have the correct binary already in our cache")
    if not os.path.exists(binary_path):
        LOG.debug("No file in cache, download %s and put it in the cache location: %s", binary_name, binary_path)
        _download_binary(version, binary_name, binary_path)
    return binary_path
