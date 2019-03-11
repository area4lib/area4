Installing
==========

*You may install in one of the following ways:*

- Through pip
- Through a requirements file

With pip
--------
To install via pip, open a terminal, and type one the following command:

.. code-block:: console

    echo Windows:
    $ pip install --upgrade area4
    echo macOS/Linux:
    $ python3 -m pip install --upgrade area4

It should install.
If the install fails because of a permissions error, try running the command with sudo or with the --user flag.

With a requirements.txt
-----------------------

To use area4 as a dependency for your project, you can add the following line:

.. code-block:: console

    area4

.. warning:: You must have prior knowledge with using a requirements file to take this path. If not, search how to use a requirements file for Python dependencies.

.. warning:: We suggest you don't use Pipfile to manage dependencies as it is still in development
