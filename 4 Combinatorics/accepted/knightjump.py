"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Knight Jump
Link:     https://open.kattis.com/contests/e7uxa8/problems/knightjump

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 16.11.2021

Method :  Backtracking, Breadth-first-search
Status :  Accepted
Runtime:  0.09 s

"""

# These are all the moves the knight can make.
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def get_next_knight_moves(x, y, n, grid):
    """
    Get the next possible knight moves from a given position.
    """
    moves = []
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#':  # Check if the move is valid. Must be in the grid and can't be blocked by a #.
            moves.append((nx, ny))
    return moves


def breadth_first_search(x, y, n, grid):
    """
    Breadth-first-search to find the shortest path to cell (0, 0).
    :param x: starting x-coordinate
    :param y: starting y-coordinate
    :param n: grid size
    :param grid: 2D-grid array (to check if cell is blocked by a #)
    :return: number of steps to reach (0, 0)
    """
    q = [(x, y, 0)]  # The q stores the current position and the number of steps taken (0 at the start).
    visited = set()

    # As long as there is someting in the queue
    while q:
        # Pop position at the top of the queue
        x, y, steps = q.pop(0)

        # If we found the start cell (0,0) return the number of steps taken
        if x == y == 0:
            return steps
        
        # Otherwise get all possible next moves for the knight and add them to the queue if they haven't already been visited
        for nx, ny in get_next_knight_moves(x, y, n, grid):
            if (nx, ny) not in visited:
                q.append((nx, ny, steps + 1))
                visited.add((nx, ny)) # Also add this new cell to visited cells
    return -1


def get_knight_pos(grid, n):
    """
    Get the starting position of the knight.
    :param grid: 2 D-grid array
    :param n: grid size
    :return: x,y coordinates of the starting position
    """
    # Iterate over all rows and columns
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'K': # If the cell at that row and column contains the knight: return the indices
                return x, y


# Read grid size
n = int(input())

# Create grid
grid = [list(input()) for _ in range(n)]

# Search for the knight on the grid and get its coordinates
x, y = get_knight_pos(grid, n)

# Search path to cell 0, 0 and print number of steps
print(breadth_first_search(x, y, n, grid))














