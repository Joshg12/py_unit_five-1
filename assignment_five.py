print("Welcome to the guessing game?") #Welcomes the user
input("What is your name?") #Asks the user's name

import random #Adds a randomizer

def get_number():
    '''
    This function choses a random number.
    '''
    randomn = random.randint(1,100) #Picks a number from 1-100
    return randomn
def get_guess():
    guess = int(input("Enter your guess")) #Gets the user's guess
    return guess

for x in range(3):
    randomn = get_number()
    while True:
        guess = get_guess()

        if randomn == guess:
            print("You guessed correctly! You have completed a round.") #When the user guesses correctly
            break
        else:
            print("You guessed incorrectly, try again.") #When the user guesses incorrectly
        if guess > randomn: print("The correct number is less than your guess.") #Helps the user guess
        if guess < randomn: print("The correct number is greater than your guess.") #Helps the user guess
