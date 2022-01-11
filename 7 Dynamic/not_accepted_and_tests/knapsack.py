


def knapsack(n, W, val, wt):
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]


def knapSack(W, wt, val):
    # Simple Checks
    if [i for i in wt if i <= 0] != []:
        print("Weights must be < 0")
        return False
    if len(wt) != len(val) and len(val) > 0:
        print("len(wt) != len(val) or len == 0")
        return False

    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    V = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                    V[i][w] = val[i - 1]

                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Gets the items in our list

    def minInList(target):
        return min([wt[j] for j in [o for o, x in enumerate(val) if x == target]])

    ans = []
    N = W
    for i in range(-1, -(len(V)), -1):
        if N > 0 and V[i][N] > 0:
            ans.append(V[i][N])
            N = N - minInList(V[i][N])


    return (K[n][W], ans)

def main():

    c, n = [int(x) for x in input().split()]
    w = []
    v = []
    for _ in range(n):
        wi, vi = [int(x) for x in input().split()]
        w.append(wi)
        v.append((vi))

    print(knapsack(n, c, v, w))


main()