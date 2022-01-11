"""
Kattis has many pairs of nice, warm, knit socks in her sock drawer that are perfect for the winter. These socks come in
a wide range of colours and types, and have all been mixed together. Each morning Kattis needs to pick two matching socks.
To find matching socks, she simply randomly takes single socks out of the drawer until she has a matching pair. It may
take a long time, for example when she keeps drawing right socks without a matching left one. How long does she need to
keep drawing socks until she is guaranteed to have a pair to wear?

Input:
Integer n

then follow n lines with a string which is the type of sock, a string that is either left, right or any and the number of
socks of that kind.


Output the minimum number of socks Kattis needs to draw to be guaranteed to get a matching pair. If it is not possible to
get a matching pair at all, output impossible

Smaple 1
3
fuzzy any 10
wool left 6
wool right 4

Ouput: 8

Sample 2
3
sports any 1
black left 6
white right 6

Ouput: impossible

Sample 3
2
warm any 5
warm left 3

Output 4
"""




d = {}



for _ in range(int(input())):
    typ, side, n = [x for x in input().split()]
    n = int(n)
    if typ not in d:
        d[typ] = {side: n}
    else:
        d[typ][side] = n

counter = 0
c_all = 0
for entry in d:
    if d[entry].get('any'):
        if d[entry].get('left') or d[entry].get('right'):
            l = d[entry].get('left', 0)
            r = d[entry].get('right', 0)
            counter += max([l, r])
            c_all += l + r + d[entry]['any']
            continue
        counter += 1
        c_all += d[entry]['any']
    else:
        l = d[entry].get('left', 0)
        r = d[entry].get('right', 0)
        counter += max([l, r])
        c_all += l + r


if counter == c_all:
    print('impossible')
else:
    print(counter+1)































