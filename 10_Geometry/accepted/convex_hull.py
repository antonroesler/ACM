"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Convex Hull
Link:     https://open.kattis.com/problems/convexhull

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 21.01.2022

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.52 s

"""

def cross_product(v1, v2):
    return (v1[0] * v2[1]) - (v2[0] * v1[1])

def clockwise_turn(pf, pt1, pt2):
    v1 = [  # vector v1 is from pf to pt1
        pt1[0] - pf[0],
        pt1[1] - pf[1]
    ]
    v2 = [  # vector v2 is from pf to pt2
        pt2[0] - pf[0],
        pt2[1] - pf[1]
    ]
    # If cross product is bigger 0, its a counter clockwise turn
    cp = cross_product(v1, v2)
    return cp > 0

def convex_hull(points):
    """Algorithm: 
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
    """
    # We sort the point by their x value
    points = sorted(points)

    # initialize lower and upper hull
    upper = [points[0], points[1]]
    lower = [points[-1], points[-2]]
    
    n = len(points)

    # Go from left to right through all points
    for i in range(2, n):
        while len(upper) > 1 and not clockwise_turn(points[i], upper[-1], upper[-2]):
            upper.pop()
        upper.append(points[i])

    # Go back from right to left through all points
    for i in range(n - 2, -1, -1):
            while len(lower) > 1 and not clockwise_turn(points[i], lower[-1], lower[-2]):
                lower.pop()
            lower.append(points[i])

    hull = upper + lower[1:-1]
    hull.reverse()
    return hull


def testcase():
    n = int(input())
    if n == 0:
        return False
    points = []
    for i in range(n):
        x, y = input().split()
        points.append([int(x), int(y)])

    if len(points)<2:
        hull = points
    else :
        hull = convex_hull(points)
    print(len(hull))
    for p in hull:
        print(f"{p[0]} {p[1]}")
    return True

while testcase():
    pass
