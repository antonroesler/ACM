

N = int(input())

t = {}

for _ in range(N):
    line = [x for x in input().split()]
    loc = line.pop(0)
    if not t.get(loc):
        t[loc] = set(line)
    else:
        t[loc] |= set(line)
    for l in line:
        if not t.get(l):
            t[l] = set([loc])
        else:
         t[l].add(loc)


start, destination = [x for x in input().split()]
q = [(start, [])]




x = True
been = set()
while q:
    node, path = q.pop(0)
    path = path.copy()
    been.add(node)
    if node == destination:
        print(" ".join(path), node)
        x = False
        break
    if node not in path:
        path.append(node)
    for n in t[node]:
        if n not in [qi[0] for qi in q] and n not in been:
            q.append((n, path))
if x:
    print("no route found")


