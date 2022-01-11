import sys


def compare(a, b):
    print(f"? {a} {b}", flush=True)
    a = input()
    return a


n = int(input())


def main():
    a = 1
    b = n
    while True:
        c = compare(a, b)
        if c == "equal":
            if a > 1 and n%2 == 0 and a+0.5 == n/2:
                return a+1
            if a == 1 and n%2 == 1:
                a += 1
                continue
            else:
                a += 1
                b -= 1
        else:
            if a < n and a+1 != b:
                a += 1
            elif b < n:
                a += 2
            else:
                b -= 1
                a -= 1
            if compare(a, b) == "equal":
                print(f"! {a - 1}", flush=True)
                return
            print(f"! {b}", flush=True)
            return

main()