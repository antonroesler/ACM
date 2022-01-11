"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Magic Trick
Link:     https://open.kattis.com/contests/kp9a7t/problems/magictrick

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

cards = input()

seen = set()  # set of seen cards

valid = 1

# We want to check if there are any duplicate chars in the string cards.
for c in cards:
    if c in seen:
        valid = 0  # If there is a duplicate, set valid to 0 and abort the loop
        break
    seen.add(c)

print(valid)