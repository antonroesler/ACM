"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Pig Latin
Link:     https://open.kattis.com/contests/qkxmff/problems/piglatin

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 08.11.2021

Method :  Ad-Hoc
Status :  Accepted
Runtime:  0.25 s
"""

# These chars are vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def transform_to_pig_latin(s):
    # Split string into a list of words
    words = s.split() 

    # Initialize empty list for the new words in pig latin
    pig_latin_sentence = []

    # Loop over every word in the sentence
    for word in words:

        # If the first char of the word is a vowel, append 'yay' at the end
        if word[0] in vowels:
            pig_latin_sentence.append(word + 'yay')
        else:
            for i in range(len(word)):
                # Otherwise we search for the index of the first vowel in the word
                if word[i] in vowels:
                    # We then move all letters before that vowel to the end of the word and also add 'ay
                    pig_latin_sentence.append(word[i:] + word[:i] + 'ay')
                    break
    # Join the list of pig latin words back to a string
    return ' '.join(pig_latin_sentence)

while True:
    try:
        # Read input string
        s = input()

        # Print the transformed string
        print(transform_to_pig_latin(s))
    except EOFError:
        break