from math import gcd


def kuerzen(p1, p2):
    ggt = gcd(p1, p2)
    r1 = p1 / ggt
    r2 = p2 / ggt
    if r2 < 0:
        r1 *= -1
        r2 *= -1
    return r1, r2


def ausgabe(r1, r2):
    print(f"{int(r1)} / {int(r2)}")


def add_sub(x1, y1, x2, y2, op):
    b1 = x1 * y2
    b2 = x2 * y1
    p2 = y1 * y2
    if op == "+":
        p1 = b1 + b2
    else:
        p1 = b1 - b2
    r1, r2 = kuerzen(p1, p2)
    ausgabe(r1, r2)


def mult(x1, y1, x2, y2):
    p1 = x1 * x2
    p2 = y1 * y2
    r1, r2 = kuerzen(p1, p2)

    ausgabe(r1, r2)


for _ in range(int(input())):
    x1, y1, op, x2, y2 = input().split()
    if op in ["+", "-"]:
        add_sub(int(x1), int(y1), int(x2), int(y2), op)
    elif op == "*":
        mult(int(x1), int(y1), int(x2), int(y2))
    else:
        mult(int(x1), int(y1), int(y2), int(x2))
