import math


class Point:
    """A class to represnet a Point that can be stored inside the quadtree."""
    def __init__(self, x, y, id=None):
        self.x = x
        self.y = y
        self.id = id 
    
    def __eq__(self, other: object) -> bool:
        return self.id == other.id

    def distance(self, other):
        """Returns distance between two points."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def pos(self):
        return [self.x, self.y]
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def closest_pair(pointsX, pointsY):
    n = len(pointsX)
    if n <= 3:
        return brute_force(pointsX)
    
    xL = pointsX[:n//2]
    xR = pointsX[n//2:]

    print(f"XL: ({len(xL)}) {xL}")
    print(f"XR: ({len(xR)}) {xR}")
    print(pointsX[n//2])
    print()
    
    xm = pointsX[n//2].x

    yL = []
    yR = []

    for p in pointsY:
        if p.x <= xm:
            yL.append(p)
        else:
            yR.append(p)
    
    dl, p11, p12 = closest_pair(xL, yL)
    dr, p21, p22 = closest_pair(xR, yR)

    dm, pm1, pm2 = dr, p21, p22


    if dl < dr:
        dm, pm1, pm2 = dl, p11, p12


    close = [p for p in pointsY if abs(p.x - xm) < dm]
    ns = len(close)
    closest, cp1, cp2  = dm, pm1, pm2

    for i in range(1, ns):
        k = i+1
        while k <= (ns-1) and close[k].y - close[i].y < dm:
            if close[k].distance(close[i]) < closest:
                closest, cp1, cp2 = close[k].distance(close[i]), close[k], close[i]
            k += 1
    return closest, cp1, cp2

    


def brute_force(points):
    a = points[0]
    b = points[1]
    d = a.distance(b)

    for p1 in points:
        for p2 in points:
            if p1 != p2:
                if p1.distance(p2) < d:
                    d = p1.distance(p2)
                    a = p1
                    b = p2
    return d, a, b
    


def testcase():
    n = int(input())
    if n == 0:
        return False
    points = []
    for i in range(n):
        x, y = input().split()
        points.append(Point(float(x), float(y), id=i))

    pointsX = sorted(points, key=lambda p: p.x)
    pointsY = sorted(points, key=lambda p: p.y)
    
    _, a, b = closest_pair(pointsX, pointsY)
    print(f"{a.x:.2f} {a.y:.2f} {b.x:.2f} {b.y:.2f}")

    
    return True

while testcase():
    pass