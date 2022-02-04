import math


class Point:
    """A class to represnet a Point that can be stored inside the quadtree."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, other):
        """Returns distance between two points."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def pos(self):
        return [self.x, self.y]


class Rectangle:
    """A class to represent a rectangle, where x and y are the center points. 
    w ist the width and h the height."""
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point:Point):
        """Returns True if the given point lies within the rectangle."""
        return (self.x - self.w/2 <= point.x <= self.x + self.w/2 \
            and self.y - self.h/2 <= point.y <= self.y + self.h/2)

    def intersects(self, other):
        """Returns True if the rectangle overlaps with a given other rectangle."""
        return not (
            self.x + self.w/2 < other.x - other.w/2 or other.x + other.w/2 < self.x - self.w/2 or
            self.y - self.h/2 > other.y + other.h/2 or other.y - other.h/2 > self.y + self.h/2
            )


    def corners(self):
        """Returns a list of the four corners of the rectangle as Point objects."""
        return [
            Point(self.x + self.w/2, self.y + self.h/2),
            Point(self.x - self.w/2, self.y + self.h/2),
            Point(self.x + self.w/2, self.y - self.h/2),
            Point(self.x - self.w/2, self.y - self.h/2)
            ]

class Circle:
    """A class to represent a circle with center x, y and radius r."""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def contains(self, point:Point):
        """Returns true if a given Point lies within the circle."""
        return point.distance(Point(self.x, self.y)) < self.r

    def intersects(self, circle):
        center_distance = Point(self.x, self.y).distance(Point(circle.x, circle.y))
        radii = self.r + circle.r
        return center_distance < radii

    def center(self):
        return Point(self.x, self.y)


class QuadTree:
    def __init__(self, area:Rectangle, capacity:int=4):
        self.area = area
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.sub_tree = []
        self.counter = 0
        self.all = []

    def insert(self, point:Point):
        self.all.append(point)
        if not self.area.contains(point):
            return False

        if not self.divided:
            if len(self.points) < self.capacity:
                self.points.append(point)
            else:
                self.subdivide()
        else:
            for tree in self.sub_tree:
                tree.insert(point)

    def subdivide(self):
        self.sub_tree.append(QuadTree(Rectangle(self.area.x + self.area.w/4 , self.area.y + self.area.h/4, self.area.w/2, self.area.h/2)))
        self.sub_tree.append(QuadTree(Rectangle(self.area.x + self.area.w/4 , self.area.y - self.area.h/4, self.area.w/2, self.area.h/2)))
        self.sub_tree.append(QuadTree(Rectangle(self.area.x - self.area.w/4 , self.area.y + self.area.h/4, self.area.w/2, self.area.h/2)))
        self.sub_tree.append(QuadTree(Rectangle(self.area.x - self.area.w/4 , self.area.y - self.area.h/4, self.area.w/2, self.area.h/2)))
        self.divided = True

    def query(self, area:Rectangle):
        """Returns all points that lie within a given area. It may return points that lie not within the area, but every point in the area is definitely."""
        points = []
        if self.area.intersects(area):
            points.extend(self.points)
            if self.divided:
                for tree in self.sub_tree:
                    points.extend(tree.query(area))
        return points

    def query_circle(self, circle:Circle):
        """Returns all points that lie within a given circle."""
        rectangle = Rectangle(circle.x, circle.y, circle.r, circle.r)
        points = self.query(rectangle)
        return [point for point in points if circle.contains(point)]



def testcase():
    n = int(input())
    if n == 0:
        return False
    qt = QuadTree(area=Rectangle(0, 0, 200000, 200000))
    a = None
    b = None
    d = 1000000
    for i in range(n):
        x, y = input().split()
        p = Point(float(x), float(y))
        for p2 in qt.query_circle(Circle(p.x, p.y, d)):
            nd = p.distance(p2)
            if nd < d:
                a = p
                b = p2
                d = nd
        qt.insert(p)

    print(f"{a.x} {a.y} {b.x} {b.y}")

    
    return True

while testcase():
    pass