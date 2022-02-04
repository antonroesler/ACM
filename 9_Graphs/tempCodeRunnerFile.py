from queue import PriorityQueue

def main():
    while True:
        n, m, q, s = [int(x) for x in input().split()]
        if n == m == q == s == 0:
            return 

        weight = [float('inf') for _ in range(n+1)]

        edges = dict()

        for _ in range(m):
            u, v, w = [int(x) for x in input().split()]
            d = edges.get(u, False)
            if d:
                d[v] = w
            else:
                edges[u] = {v:w}
    

        weight[s] = 0
        nodes_to_search = set()
        nodes_to_search.add(s)

        queue = PriorityQueue()

        queue.put((0, s))


        # While we still have unvisited nodes:
        while not queue.empty():
            _, idx = queue.get()
            for to, w in edges.get(idx, {}).items():
                new_weight = weight[idx]+w
                if weight[to] > new_weight:
                    weight[to] = new_weight
                    queue.put((new_weight, to))
                    nodes_to_search.add(to)

        for _ in range(q):
            qt = int(input())
            if qt >= n or weight[qt] == float('inf'):
                print("Impossible")
            else:
                print(weight[qt])
        print()

main()