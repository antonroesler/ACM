"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Mirror Images
Link:     https://open.kattis.com/contests/qkxmff/problems/mirror

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.08 s

"""

def reverse(matrix):
    # Backwards for loop to reverse top to bottom
    for i in range(len(matrix), 0, -1):
        # Print the line reversed from left to right
        print(matrix[i-1][::-1])



# Read number of testcases
n = int(input())

for i in range(n):
    print(f"Test {i+1}")

    # Read size of the matrix
    rows, cols = [int(x) for x in input().split()]
    matrix = []

    # loop for as many times as there are rows
    for j in range(rows):
        # For every row read the line and add it to the matrix
        matrix.append(input())
    
    # Calculate and print result
    reverse(matrix)