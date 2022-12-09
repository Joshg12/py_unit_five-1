print("Welcome to the guessing game?")
input("What is your name?")

import random

def get_number():
    randomn = random.randint(1,100)
    return randomn
def get_guess():
    guess = int(input("Enter your guess"))
    return guess


for x in range(3):
    randomn = get_number()
    while True:
        guess = get_guess()

        if randomn == guess:
            print("You guessed correctly!")
            break
        else:
            print("You guessed incorrectly, try again.")
        if guess > randomn: print("The correct number is less than your guess.")
        if guess < randomn: print("The correct number is greater than your guess.")
