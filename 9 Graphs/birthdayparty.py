



p, c = [int(x) for x in input.split()]

def is_possible(p, c):
    mtx = [[False for col in range(p)] for row in range(p)]
    paths = [0]*p
    for _ in range(c):
        i, j = [int(x) for x in input.split()]
        mtx[i, j] = True
        mtx[j, i] = True
    
    for x in range(p):
        
    
