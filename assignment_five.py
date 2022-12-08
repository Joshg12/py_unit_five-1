print("Welcome to the guessing game?")
input("What is your name?")



import random

random = (random.randint(0,9))
print (random)


def guess():
    guess = int(input("Enter your guess"))
    return guess
guess = guess()



while True:
    if  random == guess:
        print("You guessed correctly!")
        break
    else: print("You guessed incorrectly, try again.")
    guess()
    if guess > random: print("The correct number is less than your guess.")
    if guess < random: print("The correct number is greater than your guess.")