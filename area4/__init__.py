#  Copyright (c) 2018 - present RDIL.
#  You should have received a copy of the
#  MIT License with this program/distribution.
# ---------------------------------------------------
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
        """
        Inits the class
        :param self:
        :return: nothing
        """
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
        :param self:
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
        :param self:
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


    def make_div(self, unit: str, length: int = 24, start: str = '', end: str = '', literal_unit=False) -> str:
        """
        Generates and returns a custom divider
        :param self:
        :param unit: str containing a repeating unit
        :param length: The maximum length that will not be exceeded (default: 24)
        :param start: optional starting string
        :param end: optional ending string
        :param literal_unit: if True will not try to break unit down into smaller repeating subunits
        :return: a custom created divider
        :rtype: str

        :Example:
        custom_div = make_div(unit='=-', length=40, start='<', end='=>')
        note:: The generated string will be terminated at the specified length regardless
        of whether all the input strings have been fully replicated.  A unit > 1 length may
        not be able to be replicated to extend to the full length.  In this situation, the
        string will be shorter than the specified length.
        Example: unit of 10 characters and a specified length of 25 will contain 2 units for
        a total length of 20 characters.
        """

        # reduce the size if possible to extend closer to full length
        if not literal_unit:
            unit = self._reduce_to_unit(unit)
        repeats = (length - len(start + end)) // len(unit)

        return (start + unit * repeats + end)[0:length]


    def _reduce_to_unit(self, divider: str) -> str:
        """
        Reduces a repeating divider to the smallest repeating unit possible

        :param self:
        :param divider: the divider
        :return: smallest repeating unit possible
        :rtype: str

        :Example:
        'XxXxXxX' -> 'Xx'
        """
        for unit_size in range(1, len(divider) // 2 + 1):
            length = len(divider)
            unit = divider[:unit_size]
            
            # ignores mismatches in final characters
            if unit * (length // unit_size) == divider[:unit_size * (length // unit_size)]:
                return unit
        return divider  # return original if smaller unit not found
