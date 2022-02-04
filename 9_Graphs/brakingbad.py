from collections import defaultdict
from platform import node

    
def main():
    n = int(input())
    nodes = [input() for _ in range(n)]
    n_i = {v:i for i,v in enumerate(nodes)}
    e = int(input())
    edges = defaultdict(set)
    for _ in range(e):
        u1,u2 = map(lambda z: n_i[z], input().split())
        edges[u1].add(u2)
        edges[u2].add(u1)


    a = set()
    b = set()
    a.add(0)

    stack = [[i, False] for i in range(n)]
    while stack:
        node, w = stack.pop(0)
        if node in a or node in b:
            continue
        cannot = edges.get(node, {})
        a_ = True
        b_ = True
        for c in cannot:
            if c in a:
                a_ = False
            elif c in b: 
                b_ = False
        if not a_ and not b_:
            print("Impossible")
            return
        if a_ and b_:
            if w:
                a.add(node)
            else:
                stack.append([node, True])
        elif a_:
            a.add(node)
            for t in stack:
                t[1] = False
        elif b_:
            b.add(node)
            for t in stack:
                t[1] = False
        
    print(" ".join([nodes[p] for p in a]))
    print(" ".join([nodes[p] for p in b]))
            

main()