"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  How Many Digits?
Link:     https://open.kattis.com/problems/howmanydigits

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 15.11.2021

Method :  Kamenetsky’s formula
Status :  Accepted
Runtime:  0.14s
"""

import math


def findDigits(n):
    # Base cases
    if (n < 0):
        return 0
    if (n <= 1):
        return 1
    # Else we use the formula
    return kamenetsky(n)

# Kamenetsky’s formula
# https://en.wikipedia.org/wiki/Digit_sum#Kamenetsky's_formula
def kamenetsky(n):
    return math.floor((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2.0)) + 1


# Test cases
while True:
    try:
        n = int(input())
        print(findDigits(n))
    except EOFError:
        break
