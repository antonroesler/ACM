"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Exact Change
Link:     https://open.kattis.com/problems/exactchange2

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 01.12.2021

Method :  Dynamic Programming
Status :  Accepted
Runtime:  0.43 s

"""
# Read number of test cases
cases = int(input())


for _ in range(cases):
    # Read inputs
    target = int(input())
    n_bills = int(input())
    bills = [int(input()) for x in range(n_bills)]

    # Create a table DP.
    # DP[x] will be the minimum number of bills to reach x, if x is the target
    # Initialize DP table with all infinities, index 0 is 0
    dp = [float('inf')] * 10001
    dp[0] = 0

    # Iterate over every bill we have
    for b in bills:
        # For each bill start looking at 10000-b and walk backwards
        for v in range(10000-b, -1, -1):
            if dp[v] != float('inf'):  # If there is a value other than infinity at amount v
                # We know that we can reach the amount v+b by the amount in v + 1 [or if there is something in v+b that is already smaller, we leave it]
                dp[v+b] = min(dp[v+b], dp[v] + 1)

    # Search in DP for the index that is the target or the next closest (since the index is the cash we pay)
    # DP[x] is the number of bills used to reach that amount x
    for x in range(target, len(dp)):
        if dp[x] != float('inf'):
            print(x, dp[x])
            break
