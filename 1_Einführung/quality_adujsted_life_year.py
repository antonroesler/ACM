"""
Ausgew ̈ahlte Probleme aus dem ACM Programming Contest WS21/22
Problem: Quality-Adjusted Life-Year
Link: https://open.kattis.com/problems/qaly
@author Anton Roesler (anton.roesler@stud.fra-uas.de)
@version 1.0, 25.10.2021
Method : Ad-Hoc
Status : Accepted
Runtime: 0.05 s
"""
# Read number of inputs
n = int(input())
# Initialize QALY as 0
q = 0
# Read every input [quality of period i, length of period i]
# and add that quality to life time
for _ in range(n):
data = input().split()
q += float(data[0]) * float(data[1])
print(q)