import random

def game(number):

    total_chances=10

    while total_chances != 0:

        i = int(input("Enter a number to guess:"))

        if i == number:
            print("Congratulations! You guessed the correct number!")
            break

        elif i > 100 or i < 0:
            print("You Guess The Number Out of The Range!!!")

        elif i < number:
            print("You Guess a Number is Too low!")
            total_chances -= 1
            print("Remaining Chances: ", total_chances)

        elif i > number:
            print("You Guess a Number is Too high!")
            total_chances -= 1
            print("Remaining Chances: ", total_chances)


    else:
        print("Game Over")
        print("You Lost It")
        print("The Correcr Number is: ", number)

name="Guess Correct Number Game"

print(name.center(30,"*"),"\n")

print("The Number is between 0 to 100")
number=random.randint(1,100)
# print(number)

n=1

while (n!=2):

    game(number)

    print("\nIf You Want To Play Again So Press 1\nPress 2 For Quit")
    n=int(input("What's Your Choice User: "))
