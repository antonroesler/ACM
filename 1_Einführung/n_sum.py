"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  N-sum
Link:     https://open.kattis.com/contests/kp9a7t/problems/nsum

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, dd.mm.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# The First input (number of items in the line) is unnecessary in python, but we need to read it to go on
input()


# One Line solution: print the sum of the list of elements that were read from the input
print(sum([int(x) for x in input().split()]))