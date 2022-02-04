
from math import atan2

def find_min_y(points):
    """Find the point with smallest y value."""
    y = float('inf')
    idx = 0
    for i, point in enumerate(points):
        if point[1] < y:
            y = point[1]
            idx = i
        if point[1] == y:  # If same y value, use the one with smaller x value
            if point[0] < points[idx][0]:
                idx = i
    return points[idx], idx

def cross_product(v1, v2):
    return (v1[0] * v2[1]) - (v2[0] * v1[1])

def distance(p1, p2):
    return (p2[0]-p1[0])**2+(p2[1]-p1[1])**2


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
    if cp > 0:
        return -1
    elif cp < 0:
        return 1
    else: 
        return 0
        

def polar_angle(p0, p1):
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return abs(atan2(y_span,x_span))


def p_sort(p0, p1):
    r = polar_angle(p0, p1)
    if r != 0 and r != 3.141592653589793:
        return r
    # They are colinear
    d = abs(distance(p0, p1))
    if d == 0:
        return 1000000
    return 1000000/d


def convex_hull(points):

    start, idx = find_min_y(points)
    hull = []

    # put the start point to index 0
    points[0], points[idx] = points[idx], points[0]

    points = sorted(points, key = lambda p1:p_sort(start, p1), reverse=True)

    hull.append(points[0])
    hull.append(points[1])

    for i in range(2, len(points)):
        next = points[i]
        p = hull.pop(-1)

        while len(hull) > 0 and clockwise_turn(hull[-1],p, next) != -1:
            p = hull.pop(-1)
        hull.append(p)
        hull.append(points[i])
    
    last = hull.pop(-1)
    if clockwise_turn(hull[-1], last, start) != 0:
        hull.append(last)
    
    return hull



def testcase():
    n = int(input())
    if n == 0:
        return False
    points = []
    for i in range(n):
        x, y = input().split()
        points.append([int(x), int(y)])

    hull = convex_hull(points)
    print(len(hull))
    for p in hull:
        print(f"{p[0]} {p[1]}")
    return True

while testcase():
    pass
