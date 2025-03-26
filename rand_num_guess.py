#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 25 2025
# This program asks the user to guess a number between 0 and 9.
import random


def guess_number(): #Set the random number
    correct_answer = random.randint(0, 9)
    user_guess = int(input("Guess a number between 0 and 9: ")) #Get user guess

    if user_guess == correct_answer: #Display message checking the answer
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was:", correct_answer)


if __name__ == "__main__":
    guess_number()
