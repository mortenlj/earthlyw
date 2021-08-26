import os
import logging
import stat

import appdirs
import requests
from .github import GithubLite


LOG = logging.getLogger(__name__)


class InvalidBinaryNameError(Exception):
    def __str__(self):
        return f"No asset named {self.args[0]} in selected release"


def _save_binary(browser_download_url, binary_path):
    LOG.debug("Downloading %s to %s", browser_download_url, binary_path)
    resp = requests.get(browser_download_url)
    resp.raise_for_status()
    target_dir = os.path.dirname(binary_path)
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    with open(binary_path, "wb") as fobj:
        fobj.write(resp.content)
    os.chmod(binary_path, stat.S_IXUSR)


def _download_binary(version, binary_name, binary_path):
    github = GithubLite()
    repo = github.get_repo("earthly/earthly")
    if version == "latest":
        release = repo.get_latest_release()
    else:
        raise NotImplementedError("Don't know how to find versions other than `latest`")
    for asset in release.assets:
        if asset.name == binary_name:
            return _save_binary(asset.browser_download_url, binary_path)
    raise InvalidBinaryNameError(binary_name)


def provide_binary(version, binary_name):
    app_dir = appdirs.AppDirs("earthlyw", version=version)
    binary_path = os.path.join(app_dir.user_cache_dir, binary_name)
    LOG.debug("See if we have the correct binary already in our cache")
    if not os.path.exists(binary_path):
        LOG.debug("No file in cache, download %s and put it in the cache location: %s", binary_name, binary_path)
        _download_binary(version, binary_name, binary_path)
    return binary_path
