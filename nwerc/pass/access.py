def ask(s):
    print(s, flush=True)
    line = input()
    if len(line.split()) == 2:
        return True
    else:
        return int(line.split("(")[1].split(" ")[0])


def how_many_chars(s):
    a = ask(s)
    if a is True:
        return True
    return int((a-5)/9)-1

def find_char(pw, i):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for c in chars:
        pw = pw[:i] + c + pw[i+1:]
        a = how_many_chars(pw)
        if a >= i+1:
            return pw
        if a is True:
            return True


def main():
    l = 0
    for i in range(1, 21):
        r = ask(f"{'A'*i}")
        if r is True:
            return
        if r > 5:
            l = i
            break
    pw = "A"*l
    for i in range(l):
        pw = find_char(pw, i)
        if pw is True:
            return

main()

