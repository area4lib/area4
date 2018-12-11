Custom Dividers
===============

.. important:: In version 1.0.3, custom dividers were added.  They can't be saved, but will stay applied until the Python script ends.

They can be called/used/updated this way:

.. code-block:: python

    # Setting:
    area4.custom_div = str("dividertexthere")

    # Using:
    print(area4.customdiv())
    # or...
    print(area4.custom_div)

You can also generate a custom divider with the make_div function

.. code-block:: python

    # Specify a repeating unit and a maximum length
    area4.make_div('<>', length=24) # returns a string

    # Add start or end elements
    area4.make_div('=-', length=9, start='<', end='=>')    # Returns: '<=-=-=-=>'

    # Resize existing dividers
    area4.make_div(area4.divider1, 6)    # Returns: '------'

    # Setting to custom div:
    area4.custom_div = area4.make_div('<>', 24)

    # or directly printing
    print(area4.make_div('<>', 24))

    # specify an literal unit (the function will not atempt to find smaller repeating units)
    area4.make_div('<><>~', length=10, literal_unit=True) # returns '<><>~<><>~' instead of '<><><><><>'

.. warning:: The make_div function will try to replicate whole repeating units to the specified length.  The output will always be less than or equal to the specified length.  Test the output to ensure the divider looks as you would like it.
