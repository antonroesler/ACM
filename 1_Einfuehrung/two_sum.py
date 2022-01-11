"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Two-sum
Link:     https://open.kattis.com/contests/kp9a7t/problems/twosum

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# Read line 
data = input().split(" ")

# Extract the two numbers
a = data[0]
b = data[1]

# calculate sum of the two numbers
print(int(a) + int(b))