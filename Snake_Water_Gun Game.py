# Exercise

"""
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for win.

Question:-  Write a python program to create a Snake Water Gun in Python using if-else statements.
            Do not create any fancy GUI. Use proper function to check for win.

--> Mathematical Approach

                 S W G
 computer =      0 1 2
 player =  S  0  D W L
           W  1  L D W
           G  2  W L D

"""

import random

Score=0

while True:

    user = int(input("""Enter Your choice
0 for Snake
1 for Water
2 for Gun
any other number for quit

Choose: """))

    comp = random.randint(0,2)

    if user == comp:
        print("Draw")
        print("You Both Are Selected Same Option")

    elif user == 0 and comp == 1:
        print("You Win")
        print("Snake Vs Water")
        Score += 1

    elif user == 0 and comp == 2:
        print("You Lose")
        print("Snake vs Gun")
        Score -= 1

    elif user ==1 and comp==0:
        print("you Lose")
        print("Water Vs Snake")
        Score-=1

    elif user == 1 and comp == 2:
        print("you Win")
        print("Water Vs Gun")
        Score += 1

    elif user == 2 and comp == 0:
        print("You Win")
        print("Gun Vs Snake")
        Score += 1

    elif user == 2 and comp == 1:
        print("You Lose")
        print("Gun Vs Water")
        Score -= 1

    else:
        break


print("Total Score is: ",Score)
