import random


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


def kuerzen(p1, p2):
    if p1 == 0 or p2 == 0:
        r1 = 0
        r2 = 0
    else:
        ggt = gcd(p1, p2)

        r1 = p1 / ggt
        r2 = p2 / ggt

    return r1, r2

def ausgabe(r1, r2):
    return (int(r1)/int(r2))

def add_sub(x1, y1, x2, y2, op):
    b1 = x1 * y2
    b2 = x2 *y1
    p2 = y1 * y2
    if op == "+":
        p1 = b1 + b2
    else:
        p1 = b1 - b2

    r1, r2 = kuerzen(p1, p2)

    return ausgabe(r1, r2)

def mult(x1, y1, x2, y2):
    p1 = x1*x2
    p2 = y1 * y2
    r1, r2 = kuerzen(p1, p2)

    return ausgabe(r1, r2)

for x in range(1000000):
    x1 = random.randint(-10**9, 10**9)
    x2 = random.randint(-10**9, 10**9)
    y1 = random.randint(-10**9, 10**9)
    y2 = random.randint(-10**9, 10**9)
    op = random.choice(["+", "-", "*", "/"])

    if op == "+":
        my = add_sub(int(x1), int(y1), int(x2), int(y2),  op)
        actual = (x1/y1) + (x2/y2)
        if round(my, 10) != round(actual, 10):
            print(f"Problem: {x1} {x2} {op} {y1} {y2}")
    if op == "-":
        my = add_sub(int(x1), int(y1), int(x2), int(y2),  op)
        actual = (x1 / y1) - (x2 / y2)
        if round(my, 10) != round(actual, 10):
            print(f"Problem: {x1} {x2} {op} {y1} {y2}")
    elif op == "*":
        my = mult(int(x1), int(y1), int(x2), int(y2))
        actual = (x1 / y1) * (x2 / y2)
        if round(my, 10) != round(actual, 10):
            print(f"Problem: {x1} {x2} {op} {y1} {y2}")
    else:
        my = mult(int(x1), int(y1), int(y2), int(x2))
        actual = (x1 / y1) / (x2 / y2)
        if round(my, 10) != round(actual, 10):
            print(f"Problem: {x1} {x2} {op} {y1} {y2}")

