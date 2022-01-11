"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Words for Numbers
Link:     https://open.kattis.com/contests/qkxmff/problems/wordsfornumbers

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.11.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  0.06 s

"""


def convert_less_than_twenty(number):
    """Converts a number less than 20 to a written text e.g. 12 -> Twelve."""
    return {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen'
    }[str(number)]


def convert_twenty_to_ninety(number):
    """Converts a number between 20 and 90 to a written text e.g. 52 -> Fifty-two."""
    number = int(number)
    tens = number // 10
    ones = number % 10
    tenner = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }[str(tens)]
    if ones == 0:
        return tenner
    else:
        return f'{tenner}-{convert_less_than_twenty(ones)}'


def convert_number_to_words(number):
    """Converts a number to a written text e.g. 52 -> Fifty-two."""
    number = int(number)
    if number < 20:
        return convert_less_than_twenty(number)
    else:
        return convert_twenty_to_ninety(number)


def transform_numbers_to_words(line):
    """Replaces every numeric value in line e.g. 52 with the number as a written text Fifty-two."""
    words = line.split()
    for i, word in enumerate(words):
        if word.isdigit():
            words[i] = convert_number_to_words(word)
    print(' '.join(words))


while True:
    try:
        # Read intger to be converted
        line = input()

        # Calculate and print result
        transform_numbers_to_words(line)
    except EOFError:
        break