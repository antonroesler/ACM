
v = [None] * 100100
tail = [None] * 100100
pre = [None] * 100100


def ceil_index(l, r, key):
    while r-1 > 1:
        m = l + (r-l)//2
        if v[tail[m]] >= key:
            r = m
        else:
            l=m
    return r


def LIS(n: int):
    if n == 0:
        return
    for i in range(n):
        tail[i] = 0
        pre[i] = -1

    length = 1
    v = [int(x) for x in input().split()]
    for i in range(n):
        if v[i] <= v[tail[0]]:
            tail[0] = i
        elif v[i] > v[tail[length-1]]:
            pre[i] = tail[length-1]
            length += 1
            tail[length] = i
        else:
            m = ceil_index(-1, length-1, v[i])
            pre[i] = tail[m-1]
            tail[m] = i
    print(length)
    out = []
    i = tail[length-1]
    while i >= 0:
        out.append(i)
        i=pre[i]
    i = len(out)-1
    while i >= 0:
        if i < len(out)-1:
            print(' ')
        print(out[i], end='')
        i-=1


def main():
    n = int(input())
    LIS(n)


main()
