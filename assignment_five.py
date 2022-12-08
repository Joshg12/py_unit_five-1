print("Welcome to the guessing game?")
input("What is your name?")

import random

def get_number():
    randomn = random.randint(0,9)
    print (randomn)
    return randomn
get_number()
def get_guess():
    guess = int(input("Enter your guess"))
    return guess


while True:
    guess = get_guess()
    randomn = get_number()
    if random == guess:
        print("You guessed correctly!")
        break
    else: print("You guessed incorrectly, try again.")
    if guess > randomn: print("The correct number is less than your guess.")
    if guess < randomn: print("The correct number is greater than your guess.")