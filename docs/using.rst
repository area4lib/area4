Using
=====

After you install the package (see the installing section), you need to import it into any Python file that you will use it in.

You can do this by adding the following line to the top:

.. code-block:: python

    import area4

.. warning::
    Versions before 2.0 don't work with the new methods.
    1.x has reached its end-of-life, and you should migrate.
    See the migrating guide for how to do so.

If you want to you can check to make sure the library is working, you can run:

.. code-block:: python

    print(area4.area4info()) 

Now, to get dividers, use this function:

.. code-block:: python

    print(
        area4.divider(4)
    )  # This prints divider number 4 to the console

For what all the dividers look like, see the next section.
