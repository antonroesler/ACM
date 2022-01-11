"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Pot
Link:     https://open.kattis.com/contests/kp9a7t/problems/pot

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

output = 0

for i in range(int(input())):
    # Read ith input
    number = input()

    # The last digit is the power
    output += int(number[:-1])**int(number[-1])

print(output)