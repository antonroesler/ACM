"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22

Problem:  Prime Spiral
Link:     https://open.kattis.com/contests/qkxmff/problems/spiral

@author   Anton Roesler (anton.roesler@stud.fra-uas.de)
@version  1.0, 14.11.2021

Method :  Breadth first search
Status :  Accepted
Runtime:  0.15s

"""

# Four Directions: down, up, left, right
u, d, l, r = (0, -1), (0, 1), (-1, 0), (1, 0)

# Translate turn directions: after up comes left, after right comes up. etc.
turn = {u: l, r: u, d: r, l: d}


def is_prime(value):
    """
    Check if a value is prime.
    """
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


class Cell:
    """Has a value and neighbors."""
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    def neighbors(self, grid):
        """Calculates and returns all neighbor cells of this cell."""
        out = []
        for x, y, in [(self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y), (self.x, self.y - 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                out.append(grid[x][y])
        return out

    def is_valid(self):
        """Returns true if this cell's value is prime."""
        if is_prime(self.value):
            return False
        return True


def spiral(size):
    x = y = size // 2  # Start at the center

    # Initial direction is up
    dx, dy = u

    # Create matrix: 2D array with shape (size x size) all filled with None
    matrix = [[None] * size for _ in range(size)]
    count = 0


    while True:
        count += 1
        # Add current value as cell to matrix at current position
        matrix[y][x] = Cell(y, x, count) 

        # Get new direction
        new_dx, new_dy = turn[dx, dy]  

        # Get new current position
        new_x, new_y = x + new_dx, y + new_dy

        # Try to turn left
        if (0 <= new_x < size and 0 <= new_y < size and matrix[new_y][new_x] is None):  # Check if new position is inside matrix and empty
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # If turn is not possible: move straight
            x, y = x + dx, y + dy
            if not (0 <= x < size and 0 <= y < size):
                return matrix  # Finished


def two_d_array_breadth_first_search(matrix, start, target):
    """
    Breadth-first search for a 2D array.
    """
    # In the queue is the start cell together with an int that represents the depth of the search
    queue = [(start, 0)]

    # We also keep track of all the values of the cells in the queue, not a clean solution but it was necessary...
    q_values = [start.value]

    # And a set of all visited cells
    visited = set()

    # While there is something in the queue we keep looping
    while queue:

        # Get the cell next in line (FIFO)
        current, depth = queue.pop(0)
        q_values.pop(0)

        # If this cells value is the target, we are done. 
        if current.value == target:
            return current, depth  # We return the cell and the depth (number of steps from start to the cell)
        
        # Add cell to visited cells
        visited.add(current.value)

        # Get all neighbors from that cell
        for neighbor in current.neighbors(spiral_matrix):
            # If we haven't seen that neighbor before we add it to the queue.
            if neighbor.value not in visited and neighbor.value not in q_values and neighbor.is_valid():
                queue.append((neighbor, depth + 1))
                q_values.append(neighbor.value)
    
    # If there is nothing left in the queue, there is no solution
    return False, "impossible"

# V MAIN PROGRAM V

# Create Grid
spiral_matrix = spiral(101)

# Initialize testcase variable
case = 0
while True:
    case += 1
    try:
        # Read inputs as integers
        start, target = map(int, input().split())
    except:
        break
    
    # First we have to find the start cell, we can use our breadth first search and just start at the middle and use the start cell as our target, we don't care about how many steps we need
    start_cell, _ = two_d_array_breadth_first_search(spiral_matrix, spiral_matrix[50][50], start)

    # Next we use our breadth first search to find the target cell from the start cell. This time we care about the number of steps.
    _, steps = two_d_array_breadth_first_search(spiral_matrix, start_cell, target)
    
    # Print result
    print(f"Case {case}: {steps}")

















    
