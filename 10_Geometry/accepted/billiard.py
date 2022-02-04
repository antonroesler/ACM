"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Billiard
Link:     https://open.kattis.com/problems/billiard

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 18.01.2022

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.06 s
"""

import math

def testcase():
    # Read inputs
    a, b, s, m, n = [int(x) for x in input().split()]
    if a == b == s == m == n == 0:
        return False

    x = a*m # The total distance the ball moves along the x axis
    y = b*n # The total distance the ball moves along the y axis

    # Calculate the total distance that the ball moves
    total = math.sqrt(x**2 + y**2) 

    # Calculate the velocity, which is just the total distance divided by the given time
    vel = total / s

    # We can then use the acos to get the angle: 
    angle = 180 * math.acos(x/total) / math.pi

    # Print formatted output
    print(f"{angle:.2f} {vel:.2f}")
    return True

while testcase():
    pass
