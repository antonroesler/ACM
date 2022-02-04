"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Torn to Pieces
Link:     https://open.kattis.com/contests/rxgmfr/problems/torn2pieces

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 11.01.2022

Method :  BFS (and using hashmap as graph representation)
Status :  Accepted
Runtime:  0.06 s

"""

# Read number of pieces of the map
N = int(input())

# Initialize empty hashmap, the hashmap will hold a set of neighbors for every
# station
t = {}

# Iterate over every piece of the map
for _ in range(N):
    # Read input for that piece
    line = [x for x in input().split()]
    loc = line.pop(0) # Location on that piece
    # Store that location in hashmap with all neighbors 
    if not t.get(loc):
        t[loc] = set(line)  
    else:
        t[loc] |= set(line)
    # And we also need to add the location to each neighbors set
    # because the graph has no direction
    for l in line:
        if not t.get(l):
            t[l] = set([loc])
        else:
         t[l].add(loc)


# Read start and destination and initialize a queue
start, destination = [x for x in input().split()]
q = [(start, [])]


x = True
been = set()  # Set of visited locations

# BFS
# As long as there is something in the queue
while q:
    # Get node and add it to visited nodes set
    node, path = q.pop(0)
    path = path.copy()
    been.add(node)

    # If we found destination, print the path
    if node == destination:
        print(" ".join(path), node)
        x = False
        break
    
    # Otherwise we add the node to the path and to the queue
    if node not in path:
        path.append(node)
    for n in t.get(node, []):
        if n not in [qi[0] for qi in q] and n not in been:
            q.append((n, path))
# If queue is empty and we didn't find the destination, there is no path
if x:
    print("no route found")


