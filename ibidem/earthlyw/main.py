import logging
import os
import sys

import colorlog

from ibidem.earthlyw import identify


def init_logging():
    log_level = logging.WARNING
    if os.getenv("EARTHLYW_VERBOSE") is not None:
        log_level = logging.DEBUG
    root = logging.getLogger()
    root.setLevel(log_level)
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = colorlog.TTYColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
        datefmt=None,
        stream=handler.stream,
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)


def main():
    init_logging()
    log = logging.getLogger(__name__)
    version = identify.select_version()
    binary_name = identify.find_binary_name()
    log.info("See if we happen to have the correct binary already in our cache")
    log.info("Download the correct binary and put it in the cache location")
    log.info("Exec into earthly, passing along environment and args")


if __name__ == '__main__':
    main()
