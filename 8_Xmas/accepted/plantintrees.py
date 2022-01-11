n = int(input())

trees = [int(t) for t in input().split()]


trees.sort(reverse=True)

for i in range(n):
    trees[i] += i+2

print(max(trees))