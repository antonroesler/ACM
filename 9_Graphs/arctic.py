import math

N = int(input())
for TESTCASE in range(N):
    s, p = [int(x) for x in input().split()]

    coords = []

    for _ in range(p):
        c = [int(x) for x in input().split()]
        coords.append((c[0], c[1]))



    def distances(arr):
        mtx = [[float('inf') for col in arr] for row in arr]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    d = math.sqrt((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)
                    mtx[i][j] = d
        return mtx

    def no_cycle(points, i, j):
        if i in points and j in points:
            return False
        return True
    

    def kruksal(arr):
        edge_distances = []
        points = set()
        while len(edge_distances) < len(arr)-1:
            s = float('inf')
            id = 0
            jd = 0
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if arr[i][j] < s and no_cycle(points, i, j):
                        s = arr[i][j]
                        id = i
                        jd = j
            edge_distances.append(s)
            points.add(i)
            points.add(j)
            arr[id][jd] = float('inf')
            arr[jd][id] = float('inf')
        return edge_distances

    i = p-s-1 # p-2//2-2
    
    print(round(sorted(kruksal(distances(coords)))[i], 2))


# Problem: Say we have 3 s channels. Then the third one has to be at a distance of 1 to one of the other two to make sense.