from math import sqrt


def get_hexagon_perimeter_from_area(a) -> float:
    return 6 * sqrt(2*a/(3*sqrt(3)))


print(get_hexagon_perimeter_from_area(int(input())))
