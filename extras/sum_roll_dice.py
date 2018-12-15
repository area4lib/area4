import random


def roll_dice():
    sumz = 0 # will return the sum of the roll calls.
    while True:
        roll = random.randint(1, 6)
        sumz += roll
        if(input("Enter y or n to continue : ").upper()) == 'N':
            print(sumz)      # prints the sum of the roll calls
            break


roll_dice()
