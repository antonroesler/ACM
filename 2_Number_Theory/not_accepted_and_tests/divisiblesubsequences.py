


def local_input():
    return 4, 8, [2, 1, 2, 1, 1, 2, 1, 2]


def cut_ends(arr, ca):
    if arr[0] == ca:
        return [0]
    if arr[-1] == ca:
        return [-1]

def seq():
    s = [0]
    ne = 0
    for i in range(10):
        if i % 2 == 0:
            print(s)
        else:
            new = (ne+1)*-1
            if i % 3 == 0:
                ne += 1
            else:
                ne *= -1
            print(s[:-1], new)
            s.append(new)

def main(d, n, arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] % d == 0:
            counter += 1
    print(2**counter-1)

def go():
    for _ in range(int(input())):
        main(*[int(x) for x in input().split()], [ int(x) for x in input().split()])

seq()
