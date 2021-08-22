import logging
import os
import os.path
import sys

import colorlog

from ibidem.earthlyw import identify, fetch


def init_logging():
    log_level = os.getenv("EARTHLYW_LOGLEVEL", logging.getLevelName(logging.WARNING))
    if log_level is not None:
        log_level = logging.getLevelName(log_level)
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
    try:
        version = identify.select_version()
        binary_name = identify.find_binary_name()
        binary_path = fetch.provide_binary(version, binary_name)
        log.debug("Execing into earthly, passing along environment and args")
        os.execv(binary_path, ["earthly"] + sys.argv[1:])
    except Exception as e:
        log.error(str(e))
        sys.exit(-1)


if __name__ == '__main__':
    main()
