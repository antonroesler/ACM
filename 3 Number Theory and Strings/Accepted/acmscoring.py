"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  ACM Contest Scoring
Link:     https://open.kattis.com/contests/qkxmff/problems/acm

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 08.11.2021

Method :  Ad-Hoc
Status :  Accepted
Runtime:  0.06 s

"""


problems = {}  # HashMap with all problems and their times
finished = set()  # Set to keep track of all finished problems


while True:
    line = input()
    if line == "-1":
        break
    minute, problem, result = line.split()
    minute = int(minute)
    if result == "right":  # If problem was solved correctly
        if problem not in problems:  # If problem was not tried before
            problems[problem] = minute  # Add it to the HashMap
            finished.add(problem)  # Add it to finished problems
        elif problem not in finished:  # If problem was tried before
            problems[problem] += minute  # Add the time to the HashMap
            finished.add(problem)  # Add it to finished problems
    else:  # If problem was not solved correctly
        if problem in problems:  # If problem was tried before: add 20
            problems[problem] += 20
        else: # Else initialize with 20 
            problems[problem] = 20

# Sum up the score of all problems that were finished
score = sum([problems.get(k, 0) for k in finished])

# Print number of finished problems and the total score
print(len(finished), score)