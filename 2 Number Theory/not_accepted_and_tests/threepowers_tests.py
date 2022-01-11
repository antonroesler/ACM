from math import log


def PowTwoGen():
    n = 0
    while True:
        yield 3 ** n
        n += 1

power = PowTwoGen()


m = 1025
sets = [set()]
while len(sets) < m:
    p = next(power)
    for s in sets:
        if p not in s:
            new_set = set(i for i in s)
            new_set.add(p)
            sets.append(new_set)
        if len(sets) == m+1:
            break





for i, s in enumerate(sets):
    print(f"{i+1}: {s}")