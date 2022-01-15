
def get_neighbors(i, j):
    n = []
    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        n.append([i+x, j+y])
    return n

def is_border(i, j, arr):
    if i == 0 or i == len(arr) or j == 0 or j == len(arr):
        return True
    return False

def value(i, j, arr):
    return arr[i][j]

def is_lake(i, j, arr):
    seen = set()
    q = [x for x in get_neighbors(i, j)]
    while q:
        neighbor = q.pop()
        if is_border(*neighbor, arr):
            return False
        else:
            if value(*neighbor, arr) == "0" and idd(neighbor) not in seen:
                for ne in get_neighbors(*neighbor):
                    if idd(ne) not in seen:
                        q.append(ne)
                seen.add(idd(neighbor))
    return True

def idd(cell):
    i = str(cell[0])
    i += str(cell[1])
    return i

def fill_lake(i, j, arr):
    seen = set()
    arr[i][j] = "1"
    q = [x for x in get_neighbors(i, j)]
    while q:
        neighbor = q.pop()
        if value(*neighbor, arr) == "0" and idd(neighbor) not in seen:
            arr[neighbor[0]][neighbor[1]] = "1"
            seen.add(idd(neighbor))


def remove_lakes(arr):
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == "0":
                if is_lake(i, j, arr):
                    fill_lake(i,j,arr)
    return(arr)


n, m = [int(x) for x in input().split()]

t1 = []
t1.append(list("0"*(m+2)))
for _ in range(n):
    t1.append(["0"]+list(input())+["0"])
t1.append(list("0"*(m+2)))

t1 = remove_lakes(t1)

coasts = [[0 for _ in range(len(t1[0]))]for _ in range(len(t1))]


def count_coast(i, j, arr):
    val = 0
    if arr[i][j] == "1":
        ns = get_neighbors(i, j)
        for neighbor in ns:
            if value(*neighbor, arr) == "0":
                val += 1
    coasts[i][j] = val

for i in range(1, len(t1)-1):
    for j in range(1, len(t1[0])-1):
        count_coast(i, j, t1)

print(sum([sum(line) for line in coasts]))
