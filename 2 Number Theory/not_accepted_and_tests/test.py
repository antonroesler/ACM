a = [5381, 2053, 7433, 1933, 1553, 6673, 1427, 1429, 1439, 1823, 2081, 2473, 1451, 1459, 1723, 1979, 7873, 4673, 1733, 4423, 1481, 1993, 1483, 6473, 2381, 2003, 1493, 1877, 1879, 3413, 1753, 3673, 2273, 3433, 2153, 4073, 6379, 4973, 1523, 2423, 1913]
print(a)
from primepath import *

for x in a:
    n = find_pos_next(x, primes=sieve(9000))
    if 2027 in n:
        print(x)