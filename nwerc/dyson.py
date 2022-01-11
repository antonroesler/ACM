def point_is_in_polygon(point, polygon):
    """
    Determines whether a point is inside a polygon.
    """
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


points = [(1, 3), (4, 7), (-3, -2), (2, -1), (0, 0), (-1, 8), (3, -5), (5, -3)]
hull = []
points.sort(key=lambda x: [x[0], x[1]])
start = points.pop(0)

def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0 * (p1[1] - p2[1]) / (p1[0] - p2[0])


points.sort(key=lambda p: (get_slope(p, start), -p[1], p[0]))


def get_cross_product(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))



points.sort(key=lambda x: [x[0], x[1]])

hull.append(start)
points.sort(key=lambda p: (get_slope(p, start), -p[1], p[0]))
for pt in points:
    hull.append(pt)
    while len(hull) > 2 and get_cross_product(hull[-3], hull[-2], hull[-1]) < 0:
        hull.pop(-2)

hull.sort(key=lambda x: [x[0], x[1]])
print(hull)
def get_shortest_path_around_points(points, start):
    """
    Returns the shortest path around a set of points.
    """
    points = points[:]
    points.sort(key=lambda x: [x[0], x[1]])
    path = [start]
    while points:
        pt = points.pop(0)
        path.append(pt)
        while len(path) > 2 and get_cross_product(path[-3], path[-2], path[-1]) < 0:
            path.pop(-2)
    return len(path)

s1, s2 = points[0][0] -1, points[0][1]
s = (s1, s2)
p = get_shortest_path_around_points(points, s)
print(p)
