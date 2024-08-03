import random

p="HANGMAN GAME"
print(p.center(25,'*'))

words=["UMBRELLA", "COMPUTER","SMARTPHONE","PERSON","CHERRY"]

word=random.choice(words)

total_chance=7
guess_word="-"*len(word)

print(guess_word)

while total_chance!=0:

    letter=input("Enter a letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guess_word=guess_word[:index]+letter+guess_word[index+1:]
                print(guess_word)

            if guess_word==word:
                print("Congrats! You guessed the word!")
                break

    else:
        total_chance=total_chance-1
        print("Incorrect Guess")
        print("Remaining Chances are: ",total_chance)

else:
    print("Sorry you lost!")
    print("Game Over!!!")