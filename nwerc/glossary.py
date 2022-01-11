

n , w = map(int, input().split())

words = []
for _ in range(n):
    words.append(input())

l = 0
for i in range(n):
    l += len(words[i])

if l < w:
    print(' '.join(words))

