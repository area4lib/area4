Info for devs
=============

Divider Format
--------------
The format for making new dividers is:

.. code-block:: python

    # Variable:
    dividerNumber = str("dividertexthere")

    # Function
    def divNumber():
        return dividerNumber

__name__ Checking
-----------------
You can check to see if __name__ is "__main__" by running this function: 
.. code-block:: python

    # import the utilities module:  
    import area4.util  
    # run function:  
    print(area4.util.check())  
    # additionally, you can specify an __name__ to work with:  
    print(area4.util.check(str(__name__)))  
