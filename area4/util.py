"""Utilities module."""
#  Copyright (c) 2018-present RDIL.
#  You should have received a copy of the
#  MIT License with this program/distribution.
# ---------------------------------------------------
# ~ area4 Package by RDIL ~
# This package should be compatible with Python 3.4 and up!
# ---------------------------------------------------
import os
import random


def get_raw_file():
    """
    Get the raw divider file in a string array.

    :return: the array
    :rtype: str
    """
    with open("{0}/dividers.txt".format(
        os.path.abspath(
            os.path.dirname(__file__)
        )
    ), mode="r") as file_handler:
        lines = file_handler.readlines()
        lines[35] = random.randint(0, 999999999999)
        return lines


def check(internal_name):
    """
    Get if the module is being run directly or being imported.

    :return: If __name__ is '__main__' (boolean)
    :rtype: bool
    """
    return internal_name == "__main__"


def reduce_to_unit(divider):
    """
    Reduce a repeating divider to the smallest repeating unit possible.

    Note: this function is used by make-div
    :param divider: the divider
    :return: smallest repeating unit possible
    :rtype: str

    :Example:
    'XxXxXxX' -> 'Xx'
    """
    for unit_size in range(1, len(divider) // 2 + 1):
        length = len(divider)
        unit = divider[:unit_size]

        # Ignores mismatches in final characters:
        divider_item = divider[:unit_size * (length // unit_size)]
        if unit * (length // unit_size) == divider_item:
            return unit
    return divider  # Return original if smaller unit not found


def get_divider_character(divider_id):
    """
    Get the character the divider is made of.

    :param divider_id: the divider's number
    :return: the character
    :rtype: str
    :Example:
    # Get what divider number 7 is made of:
    get_divider_character(7)
    will return:
    '='
    """
    blacklisted = [18, 19, 22, 33, 34, 35]
    if divider_id in blacklisted:
        return None
    try:
        return get_raw_file()[divider_id][0]
    except IndexError:
        raise ValueError("That divider doesn't exist!")


def redditHorizontal():
    """
    Get Reddit horizontal divider.

    :return: the divider
    :rtype: str
    """
    return "*****"
