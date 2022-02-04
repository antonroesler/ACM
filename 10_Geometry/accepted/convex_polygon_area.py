"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Convex Polygon Area
Link:     https://open.kattis.com/problems/convexpolygonarea

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 18.01.2022

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.07 s

"""

# Read number of test cases
N = int(input())

def polygon(line):
    """Read kattis input and return a list of points"""
    n = int(line.pop(0))
    p = []
    for _ in range(n):
        p.append([int(line.pop(0)), int(line.pop(0))])
    return p


# Read test cases
for _ in range(N):
    line = [x for x in input().split()]
    p = polygon(line)
    area = 0
    for i in range(len(p)):
        area += (p[i][0] * p[(i+1)%len(p)][1] - p[(i+1)%len(p)][0] * p[i][1]) # Convex polygon formula
    print(abs(area) / 2)
