Migrating
=========

Here are steps required to migrate to certain versions:

1.x -> 2.x
----------

To migrate from v1, you will need to change all divider calls from:

.. code-block:: python

    area4.dividerX
    # or
    area4.divX()

Where :code:`X` is the divider number, to:

.. code-block:: python

    area4.divider(X)

2.x -> 3.x
----------

This version removed the duplicate divider (was #201), so all the dividers with
numbers/IDs BIGGER than 201 need to be shifted down by 1, so if you are using any
of those dividers, you will need to change the number. For example:

.. code-block:: python

    area4.divider(208)
    # needs to be changed to:
    area4.divider(207)

    # however, anything BELOW 201 does NOT need to be changed!
