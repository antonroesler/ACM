"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Planina
Link:     https://open.kattis.com/contests/kp9a7t/problems/planina

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 25.10.2021

Method :  Recursive 
Status :  Accepted
Runtime:  0.05 s

"""

def f(n):
    """
    Returns the number of dots in a row of a square of size n.
    The 0th iteration is the base case: 2
    The nth iteration is the recursive case:
    f(n) = f(n-1) * 2 - 1 
    """
    if n == 0:
        return 2
    else:
        return f(n-1)*2-1
        
z = int(input())

# The total number if dots is the square of the number of dots in a row
print(f(z)**2)