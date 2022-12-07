print("Welcome to the guessing game?")
input("What is your name?")



import random

random = (random.randint(0,2))
print (random)


def guess():
    guess = int(input("Enter your guess"))
    return guess
guess = guess()




if  random == guess:
    print("You guessed correctly!")

