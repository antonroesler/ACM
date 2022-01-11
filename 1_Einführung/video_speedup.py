n, p, k = [int(x) for x in input().split()]

events = [0] + [int(x) for x in input().split()] + [k]

ds = [events[i+1] - events[i] for i in range(n+1)]

print(sum([ds[i] * (1+(i*(p/100))) for i in range(n+1)]))