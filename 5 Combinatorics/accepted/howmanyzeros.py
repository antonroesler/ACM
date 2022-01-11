"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  How many 0's?
Link:     https://open.kattis.com/contests/e7uxa8/problems/howmanyzeros

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 27.11.2021

Method :  Ad-Hoc
Status :  Accepted
Runtime:  0.17 s

"""


def count_zeros_at(n, i):
    """We want to count the zeros in all numbers up to n at the ith power of ten"""
    # Divide the number by 10^i and store the remainder (modulo)
    d, remainder = divmod(n, 10 ** i)

    # Divide d by 10 and store the remainder (modulo)
    p, last_digit = divmod(d, 10)

    # If the last digit is higher than 0, we can count all powers of ten up to and including p.
    if last_digit != 0:
        return p * 10 ** i
    # Otherwise we can only count all powers of ten up to p but not including p (p-1) and we need to add the number that go from p*10**i up to p*10**i+remainder
    else:
        return (p - 1) * 10 ** i + remainder + 1


def count_zeros_up_to(n):
    zeros = 0
    for i in range(len(str(n))):
        zeros += count_zeros_at(n, i)
    return zeros


def count_zeros_in_int(n):
    """Counts the number of occurrences of the digit 0 in the integer n"""
    return str(n).count('0')


while True:
    m, n = map(int, input().split())
    if m < 0:
        break
    print(count_zeros_up_to(n) - count_zeros_up_to(m) + count_zeros_in_int(m))












