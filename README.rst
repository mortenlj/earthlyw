earthlyw
========

A wrapper for earthly_ in the vein of gradle-wrapper_.

.. _earthly: https://earthly.dev
.. _gradle-wrapper: https://docs.gradle.org/current/userguide/gradle_wrapper.html

This project will start off with "README driven development".
That is, the README describes all the wanted features, and then we try to make the project do all the things we promised it would do.

If something in this readme doesn't work, it's probably because we haven't gotten there yet.

Installation
------------

Earthlyw works by adding an executable to your project, that will download the appropriate earthly binary and use that for running earthly commands.
The benefit of using ``earthlyw`` instead of just adding the ``earthly`` binary to the project, is that ``earthlyw`` works cross-platform, on all platforms/architectures with a working Python interpreter (which should include most Linux and Mac OS setups, as well as some Windows machines).

If you already have ``earthly`` installed, you can run ``earthly github.com/mortenlj/earthlyw:main+wrapper`` in your project directory, and the wrapper will be added.

For a manual installation, go to https://github.com/mortenlj/earthlyw/releases/latest and download the latest executable, and add it to your project.

Upgrades
--------

Upgrading to the latest ``earthlyw`` is just a matter of running the installer again, but this time using the wrapper::

    ./earthlyw github.com/mortenlj/earthlyw:main+wrapper


Usage
-----

Using ``earthlyw`` is as easy as using ``./earthlyw`` everywhere you would normally write ``earthly``.

Examples::

    ./earthlyw github.com/earthly/hello-world:main+hello


Versions
--------

For now, ``earthlyw`` will just use the latest version of ``earthly``, but in the future it will be possible to select a fixed version to use.
