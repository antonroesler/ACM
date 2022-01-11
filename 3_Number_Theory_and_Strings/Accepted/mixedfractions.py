"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Mixed Fractions
Link:     https://open.kattis.com/contests/qkxmff/problems/mixedfractions

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.09 s

"""


def get_mixed_fraction(numerator, denominator):
    """
    Returns a string of the mixed fraction representation of the given
    numerator and denominator.
    """
    # Calculate the whole integer part of the fraction
    whole_number = numerator // denominator

    # Calculate remainder, which will be the new numerator, because we removed some of it which is now the whole number
    numerator = numerator % denominator

    # Print result
    print(f"{whole_number} {numerator} / {denominator}")


while True:
    # Read inputs
    n, d = [int(x) for x in input().split()]

    # End case
    if n == d == 0:
        break
    
    # Calculate and print result for that testcase
    get_mixed_fraction(n, d)


