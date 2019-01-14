#  Copyright (c) 2018 - present RDIL.
#  You should have received a copy of the 
#  MIT License with this program/distribution.

# ~ area4 Package by RDIL ~
# This package and source should be compatible with Python 3.4 and up!
# (not including the package info function; its 3.6 and up)

# Imports:
import random
import area4.util


# Class:
class Dividers:
    # Info variables:
    name = "area4"
    author = "https://github.com/RDIL"
    author_email = "me@rdil.rocks"
    support_email = "support@rdil.rocks"
    description = "Dividers in Python, the easy way!"

    # The array to store dividers in:
    dividers = []

    # Run some needed operations:
    def __init__(self):
        if not area4.util.check(internal_name=__name__):
            with open("dividers.txt", "r") as fh:
                lines = fh.readlines()
                lines[35] = random.randint(0, 999999999999)
                self.dividers = lines
        else:
            raise EnvironmentError("This file can't be run directly!")

    # Function to get a divider
    def divider(self, number: int) -> str:
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
            return self.dividers[number]

    # Info function
    def area4info(self):
        """
        Gets you some info about the package

        :return: Package info
        :rtype: str
        """
        try:
            info = f"Name: {self.name}"
            info += f"\nAuthor: {self.author}"
            info += f"\nAuthor Email: {self.author_email}"
            info += f"\nDescription: {self.description}"
            return info
        except SyntaxError:
            return "Use Python 3.6 or above to run this function."
