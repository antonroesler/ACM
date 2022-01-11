"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Kitten on a Tree
Link:     https://open.kattis.com/contests/nytf6n/problems/kitten

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 19.12.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.06 s

The idea is that we collect all paths down the tree from every node. 
We read in each line: 
X A B C
Meaning that after node X come nodes A B and C.
But we want to go down the tree. So what we know now is, that the way down 
from A is to go to X. Same for B to X and C to X. 
So we build a hashmap that tells us for every node what the next node downwards is.
To get the result, we start at where the kitten is and find the next node down,
by looking up the node in the hashmap. We Do the same for this the node we found in the 
hashmap until we reach the root. Done.
"""

# Read value of the node where the kitten sits
k = int(input())



paths = {}
i = 0

while True:
    # Read input
    line = [int(x) for x in input().split()] 
    if line[0] == -1:  # The last line will be -1 -> loop ends
        break
    n = line.pop(0)  # Read node
    if i == 0:  # In the first iteration we set the root node
        root = n
    # Set for each node in the line that n is its predecessor
    for j in line:
        paths[j] = n
    i += 1

# Print Path down, start with k
print(k, end=" ")
while True:
    if k == root: # End when we reach the root.
        break
    else:
        print(paths[k], end=" ") # Print the next node downwards
        k = paths[k] # Set k to the next node downwards
print()