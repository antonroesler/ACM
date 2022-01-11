"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Radio Commercials
Link:     https://open.kattis.com/contests/pe4egm/problems/commercials

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.12.2021

Method :  Dynamic Programming
Status :  Accepted
Runtime:  0.07 s

"""


def find_sum(arr):
    max_sum = 0
    current_sum = 0

    # iterate over every commercial
    for i in range(len(arr)):
        # Add that value to current sum
        current_sum += arr[i]
        # if we go below 0 with the current sum, we stop. And start a new sum at the next element
        if current_sum < 0:
            current_sum = 0
        # if the current sum is higher than the max sum, we make the current sum the new max sum
        elif current_sum > max_sum:
            max_sum = current_sum
    # At the end, the max sum will hold the best sequence.
    return max_sum


# Read inputs
n, cost = [int(x) for x in input().split()] # number of commercials and cost per commercial
arr = [int(x) for x in input().split()]  # Number of listeners per commercial

# Subtract cost per commercial from each commercial
for i in range(len(arr)):
    arr[i] = arr[i] - cost

# Find the biggest profit possible
sum = find_sum(arr)

print(sum)