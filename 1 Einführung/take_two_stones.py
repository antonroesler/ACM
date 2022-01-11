"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Take Two Stones
Link:     https://open.kattis.com/contests/kp9a7t/problems/twostones

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# Read input
n = int(input())

# The name is 'Alice' if the number is odd, otherwise it is 'Bob'
name = "Alice" if n%2==1 else "Bob"
print(name)