
"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Digit Sum
Link:     https://open.kattis.com/contests/pe4egm/problems/digitsum

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 04.12.2021

Method :  Dynamic Programming
Status :  Accepted
Runtime:  0.08 s

"""

# Erklärung: siehe Powerpoint Präsentation. 

def count_digit_sum(d, p):
    s = [0]*10
    s[d] = 1
    for i in range(1, d):
        s[i] += int(10**p)
    for i in range(1, 10):
        s[i] += int(d*(p*10**(p-1)))
    return s



def calc(a):
    prev = 0
    s = 0
    for i in range(len(str(a))-1, -1, -1):
        d = int(str(a//(10**i))[-1])
        sc = count_digit_sum(d, i)
        for j in range(1,10):
            s += sc[j]*j
        s += prev * d*(10**i)
        prev += d
    return s



n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a==0:
        a = 1
    print(calc(b)-calc(a-1))






