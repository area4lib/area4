"""
Utilities module.

:copyright: (c) 2018-present Reece Dunham.
:license: MIT, see LICENSE for more details.
"""

import os
import random
from functools import lru_cache


@lru_cache(maxsize=None)
def get_raw_file():
    """
    Get the raw divider file in a string array.

    Note: This function is decorated with
    :code:`functools.lru_cache`, so calling
    it a second time should be faster!

    :return: The array.
    :rtype: list
    """
    with open("{0}/dividers.txt".format(
        os.path.abspath(os.path.dirname(__file__))
    ), mode="r") as file_handler:
        lines = file_handler.readlines()
        stringbuilder = ""
        i = 0
        while i < 6:
            stringbuilder += "<>"
            i += 1
        # no longer needed
        del i
        # we need to manually inject this, GitHub thinks its
        # a conflict marker
        lines[32] = stringbuilder
        lines[35] = str(
            random.randint(0, 999999999999)
        )
        return lines


def reduce_to_unit(divider):
    """
    Reduce a repeating divider to the smallest repeating unit possible.

    This function is used by :code:`make-div`.

    :param divider: The divider.
    :type divider: str
    :return: Smallest repeating unit possible.
    :rtype: str

    :Example: 'XxXxXxX' -> 'Xx'
    """
    for unit_size in range(1, len(divider) // 2 + 1):
        length = len(divider)
        unit = divider[:unit_size]

        # Ignores mismatches in final characters:
        divider_item = divider[:unit_size * (length // unit_size)]
        if unit * (length // unit_size) == divider_item:
            return unit
    return divider  # Return original if no smaller unit


def get_divider_character(divider_id):
    """
    Get the character the divider is made of.

    :param divider_id: The divider's number.
    :type divider_id: int
    :return: The character.
    :rtype: str
    :raises ValueError: If you request an invalid divider.
    :Example:
        Get what divider 7 is made of:
        :code:`get_divider_character(7)`
        will return '='.
    """
    blacklisted = [18, 19, 22, 33, 34, 35, 222, 223, 224, 226, 233, 234, 242]
    if divider_id in blacklisted:
        return None
    try:
        return get_raw_file()[divider_id][0]
    except IndexError:
        raise ValueError("That divider doesn't exist!")


def reddit_horizontal():
    """
    Get Reddit horizontal divider.

    :return: The divider.
    :rtype: str
    """
    return "*****"


def markdown_horizontal():
    """
    Get Markdown horizontal divider.

    :return: The divider.
    :rtype: str
    """
    return "---"
