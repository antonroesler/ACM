"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Triangle Area
Link:     https://open.kattis.com/contests/kp9a7t/problems/triarea

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# Read input
data = input().split()

# Extract base and height
base = int(data[0])
height = int(data[1])

# Calculate and print area
print(base*(height/2))