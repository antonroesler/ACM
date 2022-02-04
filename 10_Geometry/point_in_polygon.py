

def read_polygon():
    """
    Reads a polygon from stdin and returns a list of points.
    """
    points = []
    for _ in range(int(input())):
        x, y = [int(x) for x in input().split()]
        points.append((float(x), float(y)))
    return points

def read_test_case():
    """
    Reads a test case from stdin and returns the start and destination.
    """
    return read_polygon()

def point_is_in_polygon(point, polygon):
    """
    Returns True if the point is in the polygon, False otherwise.
    """
    x, y = point
    polygon = polygon[:]
    polygon.append(polygon[0])
    inside = False
    for i in range(len(polygon) - 1):
        if ((polygon[i][1] > y) != (polygon[i + 1][1] > y)) and \
            (x < (polygon[i + 1][0] - polygon[i][0]) * (y - polygon[i][1]) / \
            (polygon[i + 1][1] - polygon[i][1]) + polygon[i][0]):
            inside = not inside
    return inside

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def wedge(a, b):
    a[0] * b[1] - a[1] * b[0]

def isBetween(a, b, c):
    epsilon = 0.000001
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > epsilon:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True


def point_is_on_polygon(point, polygon):
    """
    Returns True if the point is on the polygon, False otherwise.
    """
    polygon = polygon[:]
    polygon.append(polygon[0])
    for i in range(len(polygon) - 1):
        if isBetween(polygon[i], polygon[i + 1], point):
            return True
    return False

def main():
    while True:
        points = read_polygon()
        if not points:
            return
        tests = read_test_case()
        for test in tests:
            if point_is_in_polygon(test, points):
                print("in")
            else:
                if point_is_on_polygon(test, points):
                    print("on")
                else:
                    print("out")

main()