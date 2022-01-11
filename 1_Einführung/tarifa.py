"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Tarifa
Link:     https://open.kattis.com/contests/kp9a7t/problems/tarifa

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.05 s

"""

# Read input
data = int(input())
month = int(input())

# Initialize variable: Used data
used = 0

# For each month read the used data
for i in range(month):
    used += int(input())

# Calculate and print the remaining data
# In the next month there was a total of (month+1)*(data per month) data and we subtract the total used data
print((month+1)*data-used)