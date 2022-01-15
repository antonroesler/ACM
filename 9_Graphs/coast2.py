



def get_neighbors(i, j):
    return [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

def is_border(i, j, arr):
    if i == 0 or i == len(arr) or j == 0 or j == len(arr):
        return True
    return False

def value(i, j, arr):
    return arr[i][j]

def is_lake(i, j, arr):
    lake = [[i, j]]
    q = [x for x in get_neighbors(i, j)]
    seen = {idd(x) for x in q}
    while q:
        neighbor = q.pop()
        if is_border(*neighbor, arr):
            return False
        else:
            if value(*neighbor, arr) == "0":
                lake.append(neighbor)
                for ne in get_neighbors(*neighbor):
                    if idd(ne) not in seen:
                        seen.add(idd(ne))
                        q.append(ne)
    for n in lake:
        arr[n[0]][n[1]] = "1"
    return True

def idd(cell):
    return str(cell[0])+str(cell[1])

def remove_lakes(arr):
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == "0":
                is_lake(i, j, arr)
    return(arr)


n, m = [int(x) for x in input().split()]

t1 = []
t1.append(list("0"*(m+2)))
for _ in range(n):
    t1.append(["0"]+list(input())+["0"])
t1.append(list("0"*(m+2)))

t1 = remove_lakes(t1)


s = 0
for i in range(1, len(t1)-1):
    for j in range(1, len(t1[0])-1):
        if t1[i][j] == "1":
            ns = get_neighbors(i, j)
            for neighbor in ns:
                if value(*neighbor, t1) == "0":
                    s += 1

print(s)
