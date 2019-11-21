Custom Dividers
===============

You can generate a custom divider with the make_div function

.. code-block:: python

    # Specify a repeating unit and a maximum length
    area4.make_div('<>', length=24) # returns a string

    # Add start or end elements
    area4.make_div('=-', length=9, start='<', end='=>')  # Returns: '<=-=-=-=>'

    # Resize existing dividers
    area4.make_div(instanceName.divider(1), 6)  # Returns: '------'

    # Setting to custom div:
    custom_div = area4.make_div('<>', 24)

    # or directly printing
    print(area4.make_div('<>', 24))

    # specify an literal unit (the function will not attempt to find smaller repeating units)
    area4.make_div('<><>~', length=10, literal_unit=True) # returns '<><>~<><>~' instead of '<><><><><>'

.. warning::
    The make_div function will try to replicate whole repeating units to the specified length.
    The output will always be less than or equal to the specified length.
    Test the output to ensure the divider looks as you would like it.

BIG thank you to `@ninexball <https://github.com/ninexball>`_ on GitHub for making this function and maintaining it!!
