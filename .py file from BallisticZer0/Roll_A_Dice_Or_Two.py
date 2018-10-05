from random import randint
import time
import random




def One_OR_Two():  #Right here its saying that for number 1 press it will roll one dice And when number 2 pressed it will roll 2 and ect.
    if input("Do you want 1 dice or 2?  \n\1 for 1(Die) \n2 for 2(Dice)  :") == '1':
        print("The dice rolled",random.randint(1,6))
        time.sleep(1)

    else:           # here its saying that when it prints dice rolled it also prints a random randint from 1 to 6, this is also happining for the second Dice.
        print("\n\nThe dice rolled\n\n",random.randint(1,6),"\n\n","And\n\n",random.randint(1,6),"\n")
        time.sleep(1)
        # If wanted Please moditfy this to help you better under stand the random function.




        # This is saying if the input to do you want to roll a dice says y or yes then it puts a random randint from a dice.
while input("\n\nDo you want to roll a dice? [y|n]") == 'y':
    One_OR_Two()




else:
     print("Maybe next time")



# Hoped this helps under standing for the random function, i also added some time function witch you can use by just typing time.sleep(and the number of seconds you want to wait.). I reall hope this helps.
