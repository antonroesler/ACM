from math import sqrt


def sieve(n):
    primes = []
    for i in range(2, n):
        prime = True
        for p in primes:
            if p > sqrt(i):
                break
            if i % p == 0:
                prime = False
        if prime:
            primes.append(i)
    return primes


tests = []
while True:
    t = int(input())
    if t == 0:
        break
    tests.append(t)


def perfect_p_power(x):
    if t in primes:
        return 1
    else:
        for p in primes:
            i = 1
            while p ** i <= t:
                if p ** i == t:
                    return i
                i += 1
    return 1


primes = sieve(max(tests))

for t in tests:
    print(f"Testing {t}")
    print(perfect_p_power(t))
