"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Jumbo Javelin
Link:     https://open.kattis.com/contests/kp9a7t/problems/jumbojavelin

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# Read the number of javelins
n = int(input())

# Initialize length of the resulting javelin with one (because we will substract n*1 but there are only n-1 connections)
length = 1

for _ in range(n):
    # Add up all the lengths of the javelins, but remove 1 for each javelin that is used to connect two javelins.
    length += int(input())-1

print(length)