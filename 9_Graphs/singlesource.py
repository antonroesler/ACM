from queue import PriorityQueue

def main():
    while True:
        n, m, q, s = [int(x) for x in input().split()]
        if n == m == q == s == 0:
            break

        weight = [float('inf') for _ in range(n)]

        edges = dict()

        for _ in range(m):
            u, v, w = [int(x) for x in input().split()]
            d = edges.get(u, False)
            if d:
                d[v] = w
            else:
                edges[u] = {v:w}

        weight[s] = 0


        queue = PriorityQueue()

        queue.put(0)
        qm = {0:{s}}

        while not queue.empty():
            c = queue.get()
            idx = qm.get(c).pop()
            for to, w in edges.get(idx, {}).items():
                new_weight = c+w
                if weight[to] > new_weight:
                    weight[to] = new_weight
                    queue.put(new_weight)
                    if qm.get(new_weight):
                        qm.get(new_weight).add(to)
                    else:
                        qm[new_weight] = {to}

        for _ in range(q):
            qt = int(input())
            if qt >= n or weight[qt] == float('inf'):
                print("Impossible")
            else:
                print(weight[qt])
        print()

main()