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

Using functions:  

.. code-block:: python

    area4.div1()  
    area4.div2()  
    area4.div3()  
    area4.div4()  
    area4.div5()  
    area4.div6()  
    area4.div7()  
    area4.div8()  
    area4.div9()  
    area4.div10()  

And if you want to you can check to make sure the library is working:  

.. code-block:: python  

    area4.area4info()
 

Custom Dividers  
---------------

.. important:: In version 1.0.3, custom dividers were added.  They can't be saved, but will stay applied until the Python script ends.  

They can be called/used/updated this way:  

.. code-block:: python  

    # Setting:  
    area4.custom_div = str("dividertexthere")   

    # Using:  
    area4.customdiv()  
    # or...  
    print(area4.custom_div)  


.. _here: https://repl.it/@jumbocakeyumyum/area4tests
.. _`View on GitHub`: https://github.com/RDIL/area4
.. [#RDIL] <contactspaceboom@gmail.com>
