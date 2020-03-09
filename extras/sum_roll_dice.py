"""A fun little extra."""

import random


def roll_dice():
    """
    Roll a die.

    :return: None
    """
    sums = 0  # will return the sum of the roll calls.
    while True:
        roll = random.randint(1, 6)
        sums += roll
        if (input("Enter y or n to continue: ").upper()) == "N":
            print(sums)  # prints the sum of the roll calls
            break


roll_dice()
