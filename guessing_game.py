"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def start_game():
    random_number = int(random.randint(1, 10))
    attempts = 1
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    def show_score():
        print("The current high score is {} attempt(s)".format(attempts))
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                show_score()
                attempts = 1
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")

if __name__ == '__main__':
    start_game()
