"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Alphabet Spam
Link:     https://open.kattis.com/contests/qkxmff/problems/alphabetspam

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.06 s	

"""

# Read input
text = input()

# Initialize all variables to 0
count_whitespace_characters = 0
count_lowercase_letters = 0
count_uppercase_letters = 0
count_symbols = 0

# Loop over every char in the text and count the respective variable up by 1
for c in text:
    if c == '_':
        count_whitespace_characters += 1
    elif c.islower():
        count_lowercase_letters += 1
    elif c.isupper():
        count_uppercase_letters += 1
    else:
        count_symbols += 1

# Calculate sum, is is the length of the text or the sum off all counters
sum = count_whitespace_characters + count_lowercase_letters + count_uppercase_letters + count_symbols

# Print each ratio
print(count_whitespace_characters/sum)
print(count_lowercase_letters/sum)
print(count_uppercase_letters/sum)
print(count_symbols/sum)
