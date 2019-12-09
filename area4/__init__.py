"""
Main module.

:Copyright: 2018-present Reece Dunham.
:License: MIT, see LICENSE for more details.
"""

from typing import Optional  # noqa
from . import util as utils  #: Alias of the utilities module.

# Info variables:
name = "area4"
__author__ = "RDIL"
__license__ = "MIT"
author_email = "me@rdil.rocks"
description = "Dividers in Python, the easy way!"


def divider(number):
    """
    Get the divider you requested.

    :param number: The divider number (can't be 0).
    :type number: int
    :return: The requested divider
    :rtype: str
    :raises ValueError: If you request an invalid divider.
    :Example: :code:`area4.divider(3)` will return '............'
    """
    if number == 0 or type(number) != int:
        raise ValueError('Please use a number bigger then 0!')
    else:
        try:
            return utils.get_raw_file()[number].replace("\n", "")
        except IndexError:
            raise ValueError('That divider doesn\'t exist!')


def splitter(div, *args):
    """
    Split text with dividers easily.

    :return: The newly made value.
    :rtype: str
    :param div: The divider.
    :type div: str
    """
    retstr = ""
    if type(div) is int:
        div = utils.get_raw_file()[div]
    if len(args) == 1:
        return args[0]
    for s in args:
        retstr += s
        retstr += "\n"
        retstr += div
        retstr += "\n"
    return retstr


def area4info():
    """
    Get some info about the package.

    :return: Package info.
    :rtype: str
    """
    return "Name: {0}\nAuthor: {1}\nAuthor Email: {2}\nDescription: {3}".format(
        name,
        __author__,
        author_email,
        description
    )


def make_div(unit, length=24,
             start='', end='',
             literal_unit=False):
    """
    Generate a custom divider.

    :param unit: A repeating unit.
    :type unit: str
    :param length: The maximum length (won't be exceeded) (default: 24).
    :type length: Optional[int]
    :param start: Starting string.
    :type start: Optional[str]
    :param end: Ending string.
    :type end: Optional[str]
    :param literal_unit:
        If :code:`True`, it will not try to break
        unit down into smaller repeating subunits.
        Defaults to :code:`False`.
    :type literal_unit: Optional[bool]
    :return: A new, custom divider.
    :rtype: str

    :Example:
    :code:`custom_div = make_div(unit='=-', length=40, start='<', end='=>')`

    .. note::
        The generated string will be terminated
        at the specified length regardless
        of if all the input strings have been fully replicated.
        A unit > 1 length may
        not be able to be replicated to extend to the full length.
        In this situation, the
        string will be shorter than the specified length.
        Example: unit of 10 characters and a specified length of
        25 will contain 2 units for
        a total length of 20 characters.
    """
    # Reduce the size if possible to extend closer to full length:
    if not literal_unit:
        unit = utils.reduce_to_unit(unit)
    repeats = (length - len(start + end)) // len(unit)
    return (start + unit * repeats + end)[0:length]
