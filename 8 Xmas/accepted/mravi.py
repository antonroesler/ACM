"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Mravi
Link:     https://open.kattis.com/contests/nytf6n/problems/mravi

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 20.12.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.08 s

"""

import math 

n = int(input())

# Three array
flows = [0 for i in range(n)]   # Contains at index i, how many % of the parents output the ith node receives.
supers = [0 for i in range(n)]  # Contains at index i, if the ith node is a super node (0/1).
parents = [0 for i in range(n)] # Contains at index i, the number of the parent node of node i.

# Read inputs
for _ in range(n-1):
    a, b, x, t = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    flows[b] = x
    supers[b] = t
    parents[b] = a

# Read how many liquid we need at each node. 
needs = [int(x) for x in input().split()] # Contains at index i, the amount of liquid the ith node needs.



for i in range(n-1, 0, -1):
    need = needs[i]
    if supers[i] == 1: # If its a super node, we only need the square root of output as input.
        need = math.sqrt(need) 
    p = flows[i]/100
    inp = need/p  # Calculate how much the parent needs to output.
    needs[parents[i]] = max(inp, needs[parents[i]])


# Print the value that is stored in the node with index 0
print(needs[0])