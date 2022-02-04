import math

class Point:
    """A class to represnet a Point that can be stored inside the quadtree."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, other):
        """Returns distance between two points."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b
    
    def len(self):
        """Returns the length of the segment. Distance from point a to b."""
        return self.a.distance(self.b)
    
