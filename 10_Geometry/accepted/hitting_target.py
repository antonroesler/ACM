"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Hitting the Targets
Link:     https://open.kattis.com/contests/pvcykt/problems/hittingtargets

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 18.01.2022

Method :  Simple geometry
Status :  Accepted
Runtime:  0.07 s

"""


def in_circle(x, y, radius, x1, y1):
    """Returns True if the point (x, y) is in the circle with radius and center
    (x1, y1)"""
    return (x - x1) ** 2 + (y - y1) ** 2 <= radius ** 2

def in_rectangular(x1, y1, x2, y2, x, y):
    """Returns True if the point (x, y) is in the rectangle (x1, y1, x2, y2)"""
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

# Read number of target shapes
m = int(input())

# List for shapes
shapes = []

# Read shapes
for i in range(m):
    shapes.append(input().split())

# Read number of shots
n = int(input())

# For every shot
for i in range(n):
    count = 0
    x, y = [int(x) for x in input().split()]  # Read shot
    for shape in shapes:  # Check for every shape if shot is in shape
        if shape[0] == "rectangle" and in_rectangular(int(shape[1]), int(shape[2]), int(shape[3]), int(shape[4]), x, y):
            count += 1
        elif shape[0] == "circle" and in_circle(int(shape[1]), int(shape[2]), int(shape[3]), x, y):
            count += 1
    print(count)