"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Quick Brown Fox
Link:     https://open.kattis.com/contests/qkxmff/problems/quickbrownfox

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 08.11.2021

Method :  Ad-Hoc
Status :  Accepted
Runtime:  0.06 s

"""

# Loop n times, with n being the input; Today we do it in one line 
for _ in range(int(input())):
    # Read input s, the possible pangram
    s = input()
    
    # Array with missing chars
    missing = []
    
    # The 26 lowercase letters have the ASCII numbers from 97-122:
    # We check if every letter is present (lower or upper case) 
    for i in range(97, 123):
        if chr(i) not in s and chr(i).upper() not in s:
            # If it is not in the string s, then it is added to missing
            missing.append(chr(i))
        
    # If there are no missing letters, its a pangram
    if len(missing) == 0:
        print("pangram")
    # Otherwise we print the missing letters
    else:
        print("missing", "".join(sorted(missing)))

