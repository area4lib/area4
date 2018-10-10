# ~ Area4 Package by RDIL ~ 

# Package info variables:
name = "area4"
author = "https://github.com/RDIL"
author_email = "contactspaceboom@gmail.com"
description = "Dividers in Python, the easy way! Multiple different divider looks."

# Divider variables:
divider1 = str("------------------------")
divider2 = str("________________________")
divider3 = str("........................")
divider4 = str("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
divider5 = str("⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️")
divider6 = str("⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️")
divider7 = str("========================")
divider8 = str("########################")
divider9 = str("************************")
divider10 = str(",,,,,,,,,,,,,,,,,,,,,,,,")
divider11 = str("////////////////////////")
divider12 = str("||||||||||||||||||||||||")
divider13 = str("~~~~~~~~~~~~~~~~~~~~~~~~")
divider14 = str("\\\\\\\\\\\\\\\\\\\\\\\\")
divider15 = str("☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕")
divider16 = str("++++++++++++++++++++++++")
divider17 = str("r(`,,,`)r r(`,,,`)r r(`,,,`)r ")
divider18 = str("( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)")
divider19 = str("&&&&&&&&&&&&&&&&&&&&&&&&&")
divider20 = str("^^^^^^^^^^^^^^^^^^^^^^^^^")
divider21 = str(r"¯\_(ツ)_/¯   ¯\_(ツ)_/¯   ¯\_(ツ)_/¯   ¯\_(ツ)_/¯")
custom_div = str("")

# Functions:
def div1():
    return divider1

def div2():
    return divider2

def div3():
    return divider3

def div4():
    return divider4

def div5():
    return divider5

def div6():
    return divider6

def div7():
    return divider7

def div8():
    return divider8

def div9():
    return divider9

def div10():
    return divider10

def div11():
    return divider11

def div12():
    return divider12

def div13():
    return divider13

def div14():
    return divider14

def div15():
    return divider15

def div16():
    return divider16

def div17():
    return divider17

def div18():
    return divider18

def div19():
    return divider19

def div20():
    return divider20

def div21():
    return divider21
  
def customdiv():
    return custom_div


def make_div(unit: str, length: int = 24, start: str = '', end: str = '', literal_unit=False) -> str:
    """
    Generates and returns a custom divider

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
        unit = _reduce_to_unit(unit)
    repeats = (length - len(start + end)) // len(unit)

    return (start + unit * repeats + end)[0:length]


# reduces a repeating divider to the smallest repeating unit possible
# example: 'XxXxXxX' -> 'Xx'
def _reduce_to_unit(divider: str) -> str:
    for unit_size in range(1, len(divider) // 2 + 1):
        length = len(divider)
        unit = divider[:unit_size]
        remainder = length % unit_size

        # ignores mismatches in final characters
        if unit * (length // unit_size) == divider[:unit_size * (length // unit_size)]:
            return unit
    return divider  # return original if smaller unit not found


def area4info():
    info = f"Name: {name}"
    info += f"\nAuthor: {author}"
    info += f"\nAuthor Email: {author_email}"
    info += f"\nDescription: {description}"
    return info
