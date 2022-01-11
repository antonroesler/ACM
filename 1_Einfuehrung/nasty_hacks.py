"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Nasty Hacks
Link:     https://open.kattis.com/contests/kp9a7t/problems/nastyhacks

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.06 s

"""

# Read the number of test cases
n = int(input())
 
for _ in range(n):
    # Read r (revenue of not advertised), e (revenue if advertised) and c (cost of advertising)
    r, e, c = input().split()

    # Calculate the profit if adverstied
    add_profit = int(e) - int(c)
    
    # If the profit is higher than the revenue of not advertising, print "advertise"
    if add_profit > int(r):
        print('advertise')
    # If the profit is lower than the revenue of not advertising, print "not advertise"
    elif add_profit < int(r):
        print('do not advertise')
    else:
        print('does not matter')