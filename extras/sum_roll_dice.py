from random import randint
import time
import random

def roll_dice():
    sum = 0     #will return the sum of the roll calls.
    while True:
        
        roll = randint(1, 6)
        sum += roll
        
        if(input("Enter y or n to continue : ").upper()) == 'N':
            print(sum)      #prints the sum of the roll calls
            break

roll_dice()
