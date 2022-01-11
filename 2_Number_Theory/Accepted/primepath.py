"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Prime Path
Link:     https://open.kattis.com/contests/guve43/problems/primepath

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.22 s

"""

from math import sqrt


def sieve(n):
    """Returns a list of all primes up to n."""
    primes = []
    for i in range(2, n):
        prime = True
        for p in primes:
            if p > sqrt(n):
                break
            if i % p == 0:
                prime = False
        if prime:
            primes.append(i)
    return primes


def kattis_input():
	# Read number of testcase
    n = int(input())
	# Initialize list for test cases
    tests = []

	# Read each testcase and put the two inputs in a list that is than added to the testcases list
    for _ in range(n):
        tests.append(sorted([int(x) for x in input().split()]))
    return n, tests


def find_pos_next(x, primes):
    poss = []
	# Find all Numbers that are prime and have only one different digit (the amount doesn't matter)
	# The difference can be either in the ones, tens, hundreds or thousands 
    for pt in [1, 10, 100, 1000]:
        a = x // pt % 10
        for f in range(1, 9-(a-1)):
            y = x + pt * f
            if y in primes and y > 999:
                poss.append(y)
        for f in range(1, a+1):
            y = x - pt * f
            if y in primes and y > 999:
                poss.append(y)
    return poss


def get_next_paths(pos_next, primes, lookup):
    pos = []
	# Find all possible next primes for all primes in the pos list (keep track of not ending up in a infinite loop using a lookup)
    for x in pos_next:
        lookup.add(x)
        pos += (find_pos_next(x, primes))
    pos = list(set(pos)-lookup)
    return pos, lookup


def find_shortest_path(a, b, primes, i=1, lookup=None):
	# Start by initializing the lookup set
    if lookup is None:
        lookup = set()
        lookup.add(a)
	# Find all possible next primes that may follow a
    pos_next = find_pos_next(a, primes)

	# If b was found in poss next, we found the shoretest path, which has length i
    if b in pos_next:
        return i

	# Iteratively find all possible next primes until b was found or there are no more possible next primes.
    path_next, lookup = get_next_paths(pos_next, primes, lookup)
    i += 1
    while len(path_next) > 0:
		# If b was found in poss next, we found the shoretest path, which has length i
        if b in path_next:
            return i
        else:
            i += 1
            path_next, lookup = get_next_paths(path_next, primes, lookup)
    return 10000  # Return 10000 if there is no prime path


def main():
	# Read input
    n, tests = kattis_input()

	# Calculate all primes up to 9999
    primes = sieve(9999)

	# Print result for each test case
    for case in tests:
        a = case[0]
        b = case[1]
        if a == b:
            print(0)
            continue
        else:
            sp = find_shortest_path(a, b, primes)
            print(sp if sp != 10000 else "Impossible")


main()
