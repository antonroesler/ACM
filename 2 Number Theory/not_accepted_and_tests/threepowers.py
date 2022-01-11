from math import log


def PowTwoGen():
    n = 0
    while True:
        yield 3 ** n
        n += 1



def get_set(n):
    if n == 1:
        return []
    power = PowTwoGen()
    l = int(log(n, 2))
    se = 2**l
    starter = 3**l

    m = n-se
    if m > 512:
        comb = get_set(m)
        comb.append(starter)
        return comb
    sets = [set()]
    while len(sets) <= m:
        p = next(power)
        for s in sets:
            if p not in s:
                new_set = set(i for i in s)
                new_set.add(p)
                sets.append(new_set)
            if len(sets) == m+1:
                break

    final = [starter]
    for x in sets[-2]:
        final.append(x)
    final.sort()
    return final


def format(arr):
    if len(arr)==0:
        print("{ }")
        return
    print("{ ", end="")
    for i, x in enumerate(arr):
        print(x, end="")
        if (i+1)<len(arr):
            print(", ", end="")
    print(" }")


while True:
    n = int(input())
    if n==0:
        break
    elif n==2:
        print("{ 1 }")
    elif n==4:
        print("{ 1, 3 }")
    elif n==8:
        print("{ 1, 3 }")
    else:
        format(get_set(n))




