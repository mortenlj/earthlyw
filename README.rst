earthlyw
========

A wrapper for earthly_ in the vein of gradle-wrapper_.

.. _earthly: https://earthly.dev
.. _gradle-wrapper: https://docs.gradle.org/current/userguide/gradle_wrapper.html

Installation
------------

Earthlyw works by adding an executable to your project, that will download the appropriate earthly binary and use that for running earthly commands.
The benefit of using ``earthlyw`` instead of just adding the ``earthly`` binary to the project, is that ``earthlyw`` works cross-platform, on all platforms/architectures with a working bash shell (which should include most Linux and Mac OS setups, as well as some Windows machines).

If you already have ``earthly`` installed, you can run ``earthly --no-cache -a github.com/mortenlj/earthlyw:main+wrapper/earthlyw`` in your project directory, and the wrapper will be added.

For a manual installation, go to https://github.com/mortenlj/earthlyw/releases/latest and download the latest executable, and add it to your project.

Upgrades
--------

Upgrading to the latest ``earthlyw`` is just a matter of running the installer again, but this time using the wrapper::

    ./earthlyw --no-cache -a github.com/mortenlj/earthlyw:main+wrapper/earthlyw


Usage
-----

Using ``earthlyw`` is as easy as using ``./earthlyw`` everywhere you would normally write ``earthly``.

Examples::

    ./earthlyw github.com/earthly/hello-world:main+hello

Some times it can be tedious to type a relative path to the ``earthlyw`` binary.
But since it is included in the repo, adding it to your ``PATH`` isn't an option either.
If you use ``earthly`` or ``earthlyw`` a lot, it can some times be hard to remember which repo has a wrapper, and which repos just assume you have ``earthly`` on your ``PATH``.

For these cases, another bash-script is available: ``ew``.
It is designed to be plopped into any directory on your ``PATH``.
When executing this script, it will search upwards for an ``Earthfile``, and an ``earthlyw``.
In the end, it will execute your command using either the found wrapper, or the ``earthly`` command, in the directory containing the found ``Earthfile``.

Versions
--------

For now, ``earthlyw`` will just use the latest version of ``earthly``.
