"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Big Truck
Link:     https://open.kattis.com/problems/bigtruck

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, .2021

Method :  Dijkstra-Algorithm
Status :  Accepted
Runtime:  0.11 s

"""

# Number of cities
n = int(input())

# Amount to pick up in city i for each city
pickups = [int(x) for x in input().split()]

# Number of roads
m = int(input())

# Adjacency matrix: index[i][j] stores the weight of the edge from city i to city j
mtx = [[float('inf') for _ in range(n)]for _ in range(n)]

# Fill in adjacency matrix
for _ in range(m):
    a, b, d = [int(x) for x in input().split()]
    # Remove 1, because the input starts at 1 not 0
    mtx[a-1][b-1] = d
    mtx[b-1][a-1] = d


# Initialize dijkstra costs to get to each city, starts with all infinity
costs = [float('inf') for _ in range(n)]

# Will store max amount of items that can collected on the path to each city i
collected = [0 for _ in range(n)]

# Initialize both lists with the first city
costs[0] = 0
collected[0] = pickups[0]

# Set to store all visited cities
seen = set()


def next_node():
    """
    Returns the next node to visit. The next node is always the node that has
    the lowest cost to get to out of all nodes that have NOT been visited yet.
    """
    node_id = None
    node_cost = float('inf')
    for i in range(n):
        if i not in seen and costs[i]<node_cost:
            node_id = i
            node_cost = costs[i]
    return node_id

idx = next_node()

# While we still have unvisited nodes:
while idx is not None:
    # Calculate the costs to all reachable nodes from the current node idx:
    # The is just the costs to get to the current node plus the costs from 
    # that node to each respective node
    cost_from_idx = [mtx[idx][i] + costs[idx] for i in range(n)] 
    for i in range(n):
        # If we found a cheaper way to get to node i:
        if costs[i] > cost_from_idx[i]:
            costs[i] = cost_from_idx[i] # update cost to get to node i
            # Set amount of collected items
            collected[i] = collected[idx] + pickups[i] 
        # If we didn't find a cheaper way, but a way with the sam cost
        # and we can collect more items on this way, we will use that amount
        elif costs[i] == cost_from_idx[i] and \
            collected[i] < collected[idx] + pickups[i]:
            collected[i] = collected[idx] + pickups[i]
    seen.add(idx)
    idx = next_node()


# If there is no way to the destination node (-1) there will still be infinity
if costs[-1] == float('inf'):
    print("impossible")
else:
    # Otherwise we print the cost and number of collected items of the las node
    print(costs[-1], collected[-1])