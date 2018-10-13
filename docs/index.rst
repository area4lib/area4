.. Area4 documentation master file, created by
   sphinx-quickstart on Wed Oct  3 20:42:55 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Area4's documentation!
=================================

.. toctree::
    :maxdepth: 4
    :caption: Contents:

.. image:: https://snyk.io/test/github/RDIL/area4/badge.svg?targetFile=requirements.txt
    :target: https://snyk.io/test/github/RDIL/area4/
    :alt: Vulnerabilities

.. image:: https://travis-ci.com/RDIL/area4.svg?branch=master
    :target: https://travis-ci.com/RDIL/area4
    :alt: Travis Build status

.. image:: https://img.shields.io/badge/license-MIT-orange.svg
    :alt: License

.. image:: https://badge.fury.io/py/area4.svg
    :target: https://pypi.org/project/area4
    :alt: PyPi Version

.. image:: https://www.codefactor.io/repository/github/rdil/area4/badge
    :target: https://www.codefactor.io/repository/github/rdil/area4
    :alt: Code Factor status

.. image:: https://www.repostatus.org/badges/latest/active.svg
    :target: https://repostatus.org/
    :alt: Repo status

By RDIL [#RDIL]_

`View on GitHub`_

Example
=======

.. warning:: If you don't understand what we mean by dividers, fear not.  

We mean dividers that divide text in the Python console, or anything you use the library for.  

An example can be found here_. 

Divider looks
=============

*The number before it is the number used in calling it, so for example if you want divider 1, it would be area4.divider1 or area4.div1().*

1. Dashed  
2. Solid  
3. Dotted  
4. Black Squares  
5. Up arrow emojis  
6. Down arrow emojis  
7. Equal signs 
8. Hashtags 
9. Asterisks (stars) 
10. Commas 
11. Slashes
12. Broken bars (|) 
13. Tildas
14. Backslashes (not to be confused with #11) 
15. Coffee cups
16. Plus signs
17. Cthulhus
18. Lenny faces
19. And (&) signs
20. Up arrow dividers (^)
21. Shrug emojis
22-31. Numbers 1-10  
32. <>s  
33. Smiley faces I think  
34. &*s  

And more coming soon!  

Installing  
==========

*You may install in one of the following ways:*  

- Through pip  
- Through requirements.txt  

To install via pip  
------------------
To install via pip, open a terminal, and type the following command:  

.. code-block:: console

    $ pip install area4 

It should install.  

To install via requirements.txt  
-------------------------------

To use area4 as a dependency for your project, you can add the following line:  

.. code-block:: console

    area4 

You must have prior knowledge with using a requirements.txt file to take this path.  

Using  
=====

After you install the package (instructions above), you need to import it into any Python file that you will use it in. 

You can do this by adding the following line to the top: 

.. code-block:: python

    import area4

After doing so, you can use any of these methods to get a divider in your console:  

Just using plain print commands:  

.. code-block:: python

    print(area4.divider1)
    print(area4.divider2)
    print(area4.divider3)
    print(area4.divider4)
    print(area4.divider5)
    print(area4.divider6)
    print(area4.divider7)
    print(area4.divider8)
    print(area4.divider9)
    print(area4.divider10)
    print(area4.divider11)
    print(area4.divider12)
    print(area4.divider13)
    print(area4.divider14)
    print(area4.divider15)
    print(area4.divider16)
    print(area4.divider17)
    print(area4.divider18)
    print(area4.divider19)
    print(area4.divider20)
    print(area4.divider21)
    print(area4.divider22)
    print(area4.divider23)
    print(area4.divider24)
    print(area4.divider25)
    print(area4.divider26)
    print(area4.divider27)
    print(area4.divider28)
    print(area4.divider29)
    print(area4.divider30)
    print(area4.divider31)
    print(area4.divider32)
    print(area4.divider33)
    print(area4.divider34)


Using functions:  

.. code-block:: python

    print(area4.div1())
    print(area4.div2())
    print(area4.div3())
    print(area4.div4())
    print(area4.div5())
    print(area4.div6())
    print(area4.div7())
    print(area4.div8())
    print(area4.div9())
    print(area4.div10())
    print(area4.div11())
    print(area4.div12())
    print(area4.div13())
    print(area4.div14())
    print(area4.div15())
    print(area4.div16())
    print(area4.div17())
    print(area4.div18())
    print(area4.div19())
    print(area4.div20())
    print(area4.div21())
    print(area4.div22())
    print(area4.div23())
    print(area4.div24())
    print(area4.div25())
    print(area4.div26())
    print(area4.div27())
    print(area4.div28())
    print(area4.div29())
    print(area4.div30())
    print(area4.div31())
    print(area4.div32())
    print(area4.div33())
    print(area4.div34())

.. warning:: In version 1.1.0, the functions changed in the way they operated.  Before 1.1.0, the functions printed the variables, but after the release, they now just return the variable.  

And if you want to you can check to make sure the library is working:  

.. code-block:: python  

    print(area4.area4info())
 

Custom Dividers  
---------------

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

.. _here: https://repl.it/@jumbocakeyumyum/area4tests
.. _`View on GitHub`: https://github.com/RDIL/area4
.. [#RDIL] <contactspaceboom@gmail.com>
