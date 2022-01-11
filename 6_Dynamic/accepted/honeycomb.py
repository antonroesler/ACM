"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  Honeycomb Walk
Link:     https://open.kattis.com/problems/honey

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, 08.12.2021

Method :  Dynamic Programming
Status :  Accepted
Runtime:  0.11 s

"""


# There are six directions we can go to from any cell:
moves = [(1,0), (1,1), (0,1),(-1,0), (-1,-1), (0,-1)]

# Set size of the grid.
SIZE = 20

def get_moves(x, y):
    """Returns a list of tuples that represent all cells that we can go from cell with given x and y."""
    return [(x+a, y+b) for (a, b) in moves if 0 <= (x+a) < SIZE and 0 <= (y+b) < SIZE]


def get_sum_of_neighbors(x, y, GRID):
    """Returns the sum of the values that are stored in all neighbors of cell with given x and y."""
    return sum([GRID[x][y] for (x, y) in get_moves(x, y)])

def honeycomb():
    # Read number of moves for the testcase
    MOVES = int(input())

    # Base case, 0 moves -> 1 option
    if MOVES == 0:
        print(1)
        return

    # Create 2D-Grid of specified size with all 0s
    GRID = [[0 for x in range(SIZE)] for y in range(SIZE)]

    # Find mid point in grid to start from
    mid = (SIZE//2, SIZE//2)

    # All neighbors of mid will be initialized with 1.
    for (x, y) in get_moves(*mid):
        GRID[x][y] = 1

    # Now we have MOVES-1 moves left, so we iterate that many times
    for move in range(MOVES-1):
        # First we create a new grid of the same size
        NEW_GRID = [[0 for x in range(SIZE)] for y in range(SIZE)]

        # Iterate over every cell in the new grid
        for x in range(SIZE):
            for y in range(SIZE):
                # Each cell gets the value that is the sum of the values of all its neighbors
                NEW_GRID[x][y] = get_sum_of_neighbors(x, y, GRID)
        # Now the new grid becomes the grid for the nex move
        GRID = NEW_GRID
    # At the end the middle number tells us how many paths there are.
    print(GRID[SIZE // 2][SIZE // 2])



# Read number of testcases and call main function that many times.
for t in range(int(input())):
    honeycomb()



