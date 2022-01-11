


def count_digit_sum_brute(b):
    s = [0]*10
    for i in range(1, b+1):
        for x in str(i):
            s[int(x)] += 1
    return s

sc = count_digit_sum_brute(56789)
print(sc)

s = 0
for j in range(1,10 ):
    s += sc[j]*j
print(s)


sc2 = count_digit_sum_brute(1233)
print(sc2)

s2 = 0
for j in range(1,10 ):
    s2 += sc2[j]*j
print(s2)

print(s - s2)


# t = 0
# for i in [700]:#[50000, 6000, 700, 80, 9]:
#     print(f"{i}:")
#     sa = count_digit_sum_brute(0, i)
#
#     print(sa[1:])
#     s = 0
#     for i in range(10):
#         s += i*sa[i]
#     print(s)
#     t += s
# print(t)
# print(t + 5*6000 + (5+6)*700 + (5+6+7)*80 + (5+6+7+8)*9)
#
# print(f"......")
# sa = count_digit_sum_brute(0, 56789)
#
# print(sa[1:])
# s = 0
# for i in range(10):
#     s += i*sa[i]
# print(s)