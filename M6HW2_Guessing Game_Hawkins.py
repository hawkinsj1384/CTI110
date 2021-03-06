# This is a number guessing game
# November 17, 2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Jalessa Hawkins

import random

# While statement allows the program to run again if the user wants it to
while True:
    def number_guessing_game(low, high, rounds):
        # This tells the user about the game
        print("Guess a number between {low} and {high}. You have {rounds} rounds to try and guess correctly.".format(low=low, high=high, rounds=rounds))
    # Gives the program the range of random numbers
        number = random.randint(low, high)
# This gives the amount of times to run while the user guesses the number
        for _ in range(rounds):
            guess = input("Enter an integer: ")
# The user has to guess higher or lower based on the
# random number generated by the program
            try:
                integer = int(guess)
                if integer == number:
                    print('You guessed right!!')
                    return
                elif integer < number:
                    print('Try Higher')
                elif integer > number:
                    print('Try Lower')
# This is for if a user does not input the correct format for integer
            except ValueError:
                print("You must enter a valid integer.")

        print("You didn't guess correctly in {rounds} rounds.".format(rounds=rounds))
# Starts the program along with determining the number times a user can guess
    number_guessing_game(1, 100, 6)
# The program will run again if the user inputs y for yes
    answer = input('Play again? Enter y for yes or n to exit. (y/n): ')
    if answer in ('y', 'n'):
        if answer == 'y':
            continue
        else:
         print ('Goodbye')
    break
