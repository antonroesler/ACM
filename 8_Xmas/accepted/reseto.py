"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Reseto
Link:     https://open.kattis.com/contests/nytf6n/problems/reseto

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, .2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  

"""

def main():
    n, k = [int(x) for x in input().split()]

    # Initialize array with all True of size n+1 
    # The value at the ith index is True, if i is prime.
    numbers = [True]*(n+1)

    # Cross out first to numbers 0 and 1, not prime
    numbers[0] = numbers[1] = False

    # Count the number of not primes bigger than 2 that we crossed out
    counter = 0

    # Start iterating from 2 -> n+1
    for i in range(2, n+1):
        if numbers[i]:
            for j in range(i, n+1, i): # For every number that is prime, we cross all multiples of it
                if numbers[j]: # If we haven't crossed that number before, we cross it and increment the counter
                    numbers[j] = False
                    counter += 1
                    if counter == k: # Until we reach the kth number crossed 
                        print(j)
                        return
main()