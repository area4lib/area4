Using
=====

After you install the package (instructions in the installing section), you need to import it into any Python file that you will use it in.

You can do this by adding the following line to the top:

.. code-block:: python

    import area4

After doing so, you need to create an instance of the class, for example:

.. code-block:: python

    a4 = area4.Dividers()


.. warning:: Legacy versions are no longer documented and don't work.   

And if you want to you can check to make sure the library is working:

.. code-block:: python

    print(a4.area4info())

.. warning:: The area4info function will only work on Python 3.6 or above.  Keep this in mind if using it and you don't want SyntaxErrors!  


