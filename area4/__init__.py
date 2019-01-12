#  Copyright (c) 2018 - present RDIL.  You should have received a copy of the MIT License with this program/distribution.

# ~ area4 Package by RDIL ~
# This package and source should be compatible with Python 3.4 and up!
# (not including the package info function; its 3.6 and up)

# Imports:
import random

# Info variables:
name = "area4"
author = "https://github.com/RDIL"
author_email = "me@rdil.rocks"
support_email = "support@rdil.rocks"
description = "Dividers in Python, the easy way! Multiple different divider looks."

# The array to store dividers in: 
dividers = []


# Run some needed operations:
def initLib():
    with open("dividers.txt", "r") as fh:
        lines = fh.readlines()
        lines[35] = random.randint(0, 999999999999)


# Function to get a divider
def divider(number: int) -> str:
    """
    Gets you the divider you requested!
    
    :param number: the divider number (NOT 0)
    :raises: ValueError
    :return: requested divider
    :rtype: str
    
    :Example:
    area4.divider(97)
    will return 🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️
    """
    
    if number == 0:
        raise ValueError('Please use a number bigger then 0!')
    else:
        return dividers[number]

    
# Info function
def area4info():
    """
    Gets you some info about the package

    :return: Package info
    :rtype: str
    """
    try:
        info = f"Name: {name}"
        info += f"\nAuthor: {author}"
        info += f"\nAuthor Email: {author_email}"
        info += f"\nDescription: {description}"
        return info
    except SyntaxError:
        return "[SyntaxError] Please use Python 3.6 or above to run this function."


initLib()
