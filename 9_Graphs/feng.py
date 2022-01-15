N = 1
M = 1

for i in range(0, M):
    print(f"M: i={i} -> Point(0, {i}), Point({N-1}, {i})")


for i in range(1, N-1):
    print(f"N: i={i} -> Point({i}, 0), Point({i}, {M-1})")
t = sum([[2, 4], [1, 1]])