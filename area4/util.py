"""
Utilities module.

:Copyright: 2018-present Reece Dunham.
:License: MIT, see LICENSE for more details.
"""

import os
import random
from typing import List, Optional  # noqa
from functools import lru_cache


def non_single_character_dividers():
    """
    Get a list of all the "blacklisted" dividers.

    These dividers are not made of a single character.
    Some examples of this include:

    * Divider 18 - :code:`( ͡° ͜ʖ ͡°)`
    * Divider 33 - :code:`^,^,^,^,^,^,`
    * Divider 34 - :code:`&*&*&*&*&*&*`

    :return: A list of divider IDs.
    :rtype: List[int]
    """
    return [18, 19, 22, 33, 34, 35, 222, 223, 224, 226, 233, 234, 242, 244]


@lru_cache(maxsize=None)
def get_raw_file():
    """
    Get the raw divider file in a string array.

    .. note:
        This function is decorated with
        :meth:`functools.lru_cache`, so calling
        it a second time should be faster!

    :return: The array.
    :rtype: List[str]
    """
    tmp = open(
        "{}/dividers.txt".format(
            os.path.abspath(os.path.dirname(__file__))
        ),
        mode="r",
    )
    lines = tmp.readlines()
    tmp.close()
    # we need to manually inject this, GitHub thinks its
    # a conflict marker
    lines[32] = "<><><><><><>"
    lines[35] = str(random.randint(0, 999999999999))
    return lines


def reduce_to_unit(divider):
    """
    Reduce a repeating divider to the smallest repeating unit possible.

    This function is used by :meth:`make_div`.

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

        .. code-block:: python

            get_divider_character(7)
            # returns '='.
    """
    if divider_id in non_single_character_dividers():
        return ""
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


def html_horizontal(closing_tag=True):
    """
    Get HTML horizontal divider.

    :param closing_tag: If a closing tag should be added.
    :type closing_tag: Optional[bool]
    :return: The HTML tag (the divider).
    :rtype: str
    """
    if closing_tag:
        return "<hr></hr>"
    return "<hr>"
