import sys
import threading
from json import JSONDecodeError
from urllib.error import HTTPError, URLError

import requests
from requests.exceptions import ConnectionError

from errbot import BotPlugin
from errbot.utils import version2tuple
from errbot.version import VERSION

HOME = "https://errbot.io/versions.json"

installed_version = version2tuple(VERSION)

PY_VERSION = ".".join(str(e) for e in sys.version_info[:3])


class VersionChecker(BotPlugin):
    connected = False
    activated = False

    def activate(self):
        if self.mode not in (
            "null",
            "test",
            "Dummy",
            "text",
        ):  # skip in all test confs.
            self.activated = True
            self.version_check()  # once at startup anyway
            self.start_poller(3600 * 24, self.version_check)  # once every 24H
            super().activate()
        else:
            self.log.info(f"Skip version checking under {self.mode} mode.")

    def deactivate(self) -> None:
        self.activated = False
        super().deactivate()

    def _get_version(self) -> str:
        """Get errbot version based on Python version."""
        version = VERSION
        major_py_version = PY_VERSION.partition(".")[0]

        # noinspection PyBroadException
        try:
            possible_versions = requests.get(HOME).json()
            version = possible_versions.get(
                f"python{major_py_version}", VERSION
            )
            self.log.debug(f"Latest Errbot version is: {version}")
        except (HTTPError, URLError, ConnectionError, JSONDecodeError):
            self.log.info("Could not establish connection to retrieve latest version.")
        return version

    def _async_vcheck(self) -> None:
        current_version_txt = self._get_version()
        self.log.debug("Installed Errbot version is: %s", current_version_txt)
        current_version = version2tuple(current_version_txt)
        if installed_version < current_version:
            self.log.debug(
                f"A new version {current_version_txt} has been found, notify the admins!"
            )
            self.warn_admins(
                f"Version {current_version_txt} of Errbot is available. "
                f"http://pypi.python.org/pypi/errbot/{current_version_txt}. "
                f"To disable this check do: {self._bot.prefix}plugin blacklist VersionChecker"
            )

    def version_check(self) -> None:
        if not self.activated:
            self.log.debug("Version check disabled")
            return
        self.log.debug("Checking version in background.")
        threading.Thread(target=self._async_vcheck).start()

    def callback_connect(self) -> None:
        if not self.connected:
            self.connected = True
