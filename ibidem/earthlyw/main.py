import logging
import os
import sys

import colorlog


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
    log.info("Figure out which version of earthly we need")
    log.info("See if we happen to have the correct binary already in our cache")
    log.info("Check which os and arch we're on")
    log.info("Download the correct binary and put it in the cache location")
    log.info("Exec into earthly, passing along environment and args")


if __name__ == '__main__':
    main()
