import math 

def hypo(H, v):
    return H / (math.sin(math.radians(v)))

H, v = [int(x) for x in input().split()]

if 0 <= v <= 180:
    print('safe')
else:
    print(int(abs(hypo(H, v))))