from math import sqrt, log, floor


def prime_factors(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x //= 2
    for i in range(3, int(sqrt(x)) + 1, 2):
        while x % i == 0:
            factors.append(i)
            x //= i
    if x > 2:
        factors.append(x)
    return count_numbers(factors)

def count_numbers(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = arr.count(i)
    return d





def main():
    n, m = map(int, input().split())
    if n == 0:
        n_ = 1
    else :
        n_ = n
    if m == 0:
        print(f"{m} does not divide {n}!")
        return
    if m == 1:
        print(f"{m} divides {n}!")
        return
    m_facs = prime_factors(m)
    for factor in m_facs:
        upper = floor(log(n_, factor))
        if upper - floor(upper) >= 0:
            upper += 1
        if not sum([n_/(factor**k) for k in range(1, upper)]) >= m_facs[factor]:
            print(f"{m} does not divide {n}!")
            return False
    print(f"{m} divides {n}!")
    return True



while True:
    try:
        main()
    except EOFError:
        break
