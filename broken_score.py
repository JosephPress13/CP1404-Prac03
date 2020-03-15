"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

import random

def main():
    score = float(input("Enter score: "))
    print(get_grade(score))
    score = random.randint(0,100)


def get_grade(score):
    if score > 100:
        return "Invalid score"
    elif score > 89:
        return "Excellent"
    elif score > 49:
        return "Passable"
    else:
        return "Bad"


main()