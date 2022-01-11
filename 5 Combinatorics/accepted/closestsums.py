"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Closest Sums
Link:     https://open.kattis.com/contests/zr36jo/problems/closestsums

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 27.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.15 s

"""
def main(n, x):
    # Read input values
    ms = [int(input()) for _ in range(n)]

    # Sort values
    ms.sort()

    # Read number of testcases for this set of values
    t = int(input())


    def find_closest(ms, ti):
        """Returns the sum of two values of list ms whose sum is the closest to ti of all two sums in ms"""

        # Initiate closest being the sum of the first two elements
        closest = ms[0] + ms[1]


        # Find the two values whose sum is closest to ti, by combining all possible combinations using two for loops
        for i in range(len(ms)):
            for j in range(i+1, len(ms)):
                # If the absolute difference between the sum of the two to the target ti is smaller then the current closest sum, this is the new closest
                if abs(ms[i] + ms[j] - ti) < abs(closest - ti): 
                    closest = ms[i] + ms[j]

        return closest

    # Print number of test case because kattis wants that
    print(f"Case {x}:")

    # Loop for as many times as there are testcases for this set of values
    for i in range(t):
        # Read target
        ti = int(input())

        # Find closest sum
        s = find_closest(ms, ti)

        # Print result
        print(f"Closest sum to {ti} is {s}.")


x = 0
while True:
    x += 1 # Number of testcase
    try:
        # Read number of elements in set
        n = int(input())

        # Call main function to start program
        main(n, x)
    
    except EOFError: # End of testcases
        break





