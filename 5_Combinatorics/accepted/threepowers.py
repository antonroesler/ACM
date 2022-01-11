"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Three Powers
Link:     https://open.kattis.com/contests/qkxmff/problems/threepowers

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 03.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.13 s

"""

from math import log


def PowTwoGen():
    n = 0
    while True:
        yield 3 ** n
        n += 1



def get_set(n:int):
    # Base cases: 
    if n <= 0 :
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [3]
    
    # Creating a generator object that yields powers of three
    power = PowTwoGen()

    # Take integer part the log2 of n. The lth power of three will be the biggest number in the set.
    l = int(log(n, 2))

    # Raise 2 to the power of l, to get the closest power of 2 to n, that is smaller or equal to n
    se = 2**l

    # Calculate the lth power of three. It is the biggest number in the set.
    starter = 3**l

    # The remaining numbers in the set are the numbers in the set with the index that n differs from the next smaller power of 2: (n-se)
    m = n-se

    # Calculate that set recursively 
    comb = get_set(m)

    # Add the biggest number to the set
    comb.append(starter)

    # Sort and return set
    comb.sort()
    return comb



def format(arr):
    """Function to print the set in the way kattis needs it. { a, b, c, ... n }"""
    if len(arr)==0:
        print("{ }")
        return
    print("{ ", end="")
    for i, x in enumerate(arr):
        print(x, end="")
        if (i+1)<len(arr):
            print(", ", end="")
    print(" }")


# Main program
while True:
    # Read input
    n = int(input())

    # Zero marks end of test
    if n==0:
        break
    n = n-1
    format(get_set(n))
