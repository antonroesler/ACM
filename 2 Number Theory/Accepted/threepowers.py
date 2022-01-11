from math import log
"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Three Powers
Link:     https://open.kattis.com/users/antonroesler/submissions/threepowers

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 03.11.2021

Method :  Recursion
Status :  Accepted
Runtime:  0.13


Erklärung: 
Die Sets starten mit: 
1
3
1, 3
9
1, 9
3, 9
1, 3, 9
27

Jedes mal wenn eine neue Power von 3 einzeln in einem set erscheint, sind die folgenden Sets ganz einfach alle vorherigen Sets plues jeweils die neue Power:
Außerdem ist jedes set welches eine Power von 2 ist eines der Sets welche die nächste Power von 3 einführt.
Daher ist das Set mit Index 2**x, das set welches einzig und allein die Zahl 3**(log(x, 2)) enthält.

Nehmen wir das set mit index 2**9 (=512)
log(512, 2) = 9
Das Set 512 ist der das Set { 19683 }  (19683=3**9)

Nun ist es auch sehr einfach jedes andere Set zu finden: 
Nehmen wir das Set 527:
log(527, 2) = 9.xxxxxx (Uns interessiert nur die 9)
Wir wissen nun dass das Set 527 mit 3**9 enden muss, das 512  die nächst kleiner Zweierpotenz von 527 ist und log(512, 2) gleich 9 ist.
Die Frage ist nun: Was ist mit den restlichen Zahlen in dem Set?
Die Antwort ist einfach: Nach dem set 512 ({ 19683 }) folgen die Sets von vorne + das set 512
Set 513 = Set 1 + Set 512 = { 1 } + { 19683 }
Set 514 = Set 2 + Set 512 = { 3 } + { 19683 }
Set 515 = Set 3 + Set 512 = { 1, 3 } + { 19683 }
...
Daher ist das Set 527 ganz einfach das Set 15 (15=527-512) + Das Set 512.

Nun finden wir rekursiv nach der selben Logik das Set 15 usw.
"""


def get_set(n: int):
    # Basic cases 0, 1, 2:
    if n <= 0:
        return []
    if n == 1:
        return [1]

    l = int(log(n, 2))  # l is the log2 of n, but we only care about the whole number part.
    se = 2 ** l         # se is the closest power of two below n.
    starter = 3 ** l    # starter is 3 to l (starter will be the last number in the set)

    m = n - se          # As starter is the last number in the resulting set, we need to calculate the rest of the set which is the same set as the set with index n-se
    comb = get_set(m)
    comb.append(starter)
    comb.sort()
    return comb


def format(arr):
    """Format the array in the way desired by kattis."""
    if len(arr) == 0:
        print("{ }")
        return
    print("{ ", end="")
    for i, x in enumerate(arr):
        print(x, end="")
        if (i + 1) < len(arr):
            print(", ", end="")
    print(" }")


while True:
    n = int(input())
    if n == 0:  # If the input is 0 the test is over, as defined by kattis.
        break
    n = n - 1  # My Algorithm uses n-1 as it assumes indexes start with 0 not with 1
    format(get_set(n))
