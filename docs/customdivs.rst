Custom Dividers
===============

You can generate a custom divider with the make_div function

.. code-block:: python

    # Specify a repeating unit and a maximum length
    instanceName.make_div('<>', length=24) # returns a string

    # Add start or end elements
    instanceName.make_div('=-', length=9, start='<', end='=>')    # Returns: '<=-=-=-=>'

    # Resize existing dividers
    instanceName.make_div(instanceName.divider(1), 6)    # Returns: '------'

    # Setting to custom div:
    instanceName.custom_div = area4.make_div('<>', 24)

    # or directly printing
    print(instanceName.make_div('<>', 24))

    # specify an literal unit (the function will not atempt to find smaller repeating units)
    instanceName.make_div('<><>~', length=10, literal_unit=True) # returns '<><>~<><>~' instead of '<><><><><>'

.. warning:: The make_div function will try to replicate whole repeating units to the specified length.  The output will always be less than or equal to the specified length.  Test the output to ensure the divider looks as you would like it.

BIG thank you to @ninexball on GitHub for making this function and maintaining it!!  
