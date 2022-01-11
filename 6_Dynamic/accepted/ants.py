"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Ants
Link:     https://open.kattis.com/contests/pe4egm/problems/ants

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 09.12.2021

Method :  Dynamic Programming 
Status :  Accepted
Runtime:  0.42 s

"""

def get_min_max_duration(l, v):
    # Initiate lo (the min durantion) and hi (the max duration); we just use the values for the first ant in the array to do it.
    lo = min(v[0], l-v[0])
    hi = max(v[0], l - v[0])

    # Iterate over every ant
    for i in v:
        # Keep the value if it is bigger/lower or use the value of the current ant
        lo = max(lo, min(i, l-i))  # lo is just the highest distance that any ant has to it's closer side. Because this is the min time that it takes if all ants run straight to the edge.
        hi = max(hi, max(i, l-i))  # hi is just the highest distance that any ant has to it's further away side. Because this is the distance it will walk as its maximum.

    return lo, hi

for _ in range(int(input())):
    l, n = [int(x) for x in input().split()] # length of pole and number of ants
    v = []  # position of the ants
    while len(v) < n:
        v += [int(x) for x in input().split()]
    lo, hi = get_min_max_duration(l, v)
    print(f"{lo} {hi}")

