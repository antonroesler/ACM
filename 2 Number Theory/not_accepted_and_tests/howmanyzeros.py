"""
Input consists of a sequence of lines. Each line contains two integers m and n. m>n.
How many 0 digits are there in the decimal representation of numbers from m to n?
"""

def main():
    """
    Main function.
    """
    while True:
        try:
            m, n = map(int, input().split())
            if m > n:
                raise ValueError
            print(howmanyzeros(m, n))
        except ValueError:
            break

def howmanyzeros(m, n):
    """
    Count the number of 0 digits in the decimal representation of numbers from m to n.
    """
    count = 0
    while m <= n:
        count += count_0s(m)
        m *= 10
    return count

count_0s = lambda n: len(str(n)) - len(str(n).rstrip('0'))


main()
