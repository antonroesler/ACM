



def is_valid_exchange(arr, i, j):
    if i == j:
        return True
    for k in range(i, j):
        if arr[k] > min(arr[i], arr[j]):
            return False
    return True

# n = int(input())
# arr = list(map(int, input().split()))
# goal = list(map(int, input().split()))

arr = [0,0,3,1,3,2]
goal = [2,1,3,0,3,0]

s = 0
i = 0
steps = []

while arr != goal and len(steps) < 2*10**5:
    if goal[i] != arr[i]:
        j = arr[s:].index(goal[i]) + s
        while i < j:
            if is_valid_exchange(arr, i, j):
                arr[i], arr[j] = arr[j], arr[i]
                steps.append((i+1, j+1))
                i = 0
                s = 0
                break
            i += 1
    else:
        i += 1
        s += 1

print(len(steps))
for s in steps:
    print(s[0], s[1])

