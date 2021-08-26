import requests

from collections import namedtuple

Release = namedtuple("Release", ("name", "draft", "prerelease", "assets"))
Asset = namedtuple("Asset", ("name", "browser_download_url"))


class GithubLite:
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "github.com/mortenlj/earthlyw"
        })

    def get_repo(self, repo_name):
        return Repository(self._session, repo_name)


class Repository:
    def __init__(self, session: requests.Session, repo_name: str):
        self._session = session
        self._repo_name = repo_name

    def get_latest_release(self):
        resp = self._session.get(f"https://api.github.com/repos/{self._repo_name}/releases/latest")
        resp.raise_for_status()
        data = resp.json()
        release_data = {f: data[f] for f in Release._fields}
        assets = []
        for data in release_data["assets"]:
            asset_data = {f: data[f] for f in Asset._fields}
            assets.append(Asset(**asset_data))
        release_data["assets"] = assets
        return Release(**release_data)
