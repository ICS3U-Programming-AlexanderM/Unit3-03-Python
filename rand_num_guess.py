#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 9, 2021
# This program gets the user to guess a number
# between 0 and 9 and tells them if it is correct.
import random


def main():
    # this function checks the user's number

    # set the correct number
    correct = random.randint(0, 9)

    # input
    user_number = float(input("Enter your number: "))
    print("")

    # check number size
    if user_number >= 10:
        print("Number must be between 0 and 9.")

    elif user_number <= -1:
        print("Number must be between 0 and 9.")

    # process & output
    elif user_number == correct:
        print("Correct!")

    else:
        print("Wrong, the number was {}.". format(correct))


if __name__ == "__main__":
    main()
