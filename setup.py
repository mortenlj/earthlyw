#!/usr/bin/env python

from setuptools import setup

setup(
    name="earthlyw",
    version="0.1",
    packages=[
        "ibidem",
        "ibidem.earthlyw",
    ],
    install_requires=[
        "setuptools",
        "colorlog<6"
    ],
    extras_require={
        "dev": [
            "tox",
            "pytest",
            'pytest-xdist',
            'pytest-sugar',
            'pytest-html',
            'pytest-cov',
        ]
    },
    namespace_packages=["ibidem"],
    zip_safe=True,

    # Metadata
    author="Morten Lied Johansen",
    author_email="mortenjo@ifi.uio.no",
    license="LGPL",
    keywords="ibidem earthly",
    url="https://github.com/mortenlj/earthlyw",

    # Entry points
    entry_points={
        "console_scripts": [
            "earthlyw = ibidem.earthlyw.main:main",
        ],
    },
)
