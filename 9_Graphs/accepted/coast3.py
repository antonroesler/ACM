"""
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  
Link:     

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, .2021

Method :  Breadth first Search 
Status :  Accepted
Runtime:  1.61 s

My approach here is, too traverse over all cells that are sea and count
for each cell how much coast it has around it.

I start by collecting all cells that are at the border and put them in a queue,
if the are water. If they are land, i count it as coast.
Then i start popping from the q. For every cell i count how much land is around
it -> km of coast line. Then i add every neighbor, that is water, 
also to the q if i wasn't visited yet. Until the queue is empty,
every sea cell has been visited exactly once.

"""
# Read grid size
N, M = [int(x) for x in input().split()]

# Initialize and fill grid
grid = []
for _ in range(N):
    grid.append(list(input()))


class Point:
    """Every point in the grid can be turned in to a point, 
    that has all required methods."""
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.value = grid[x][y]
    
    def __eq__(self, other: object) -> bool:
        """A point is equal to another if they have the x and y value."""
        return self.x == other.x and self.y == other.y
    
    def is_corner(self):
        """Returns True if the cell is in one of the four corners"""
        if  (self.x == 0 and self.y == 0)   or \
            (self.x == 0 and self.y == M-1) or \
            (self.x == N-1 and self.y == 0) or \
            (self.x == N-1 and self.y == M-1):
            return True
        return False
    
    def n(self):
        """Returns a list of all neighbors of the current point also as 
        point objects."""
        ps = []
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = self.x + x, self.y + y
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                ps.append(Point(nx, ny))
        return ps
    
    def __hash__(self):
        """Required to put points into a set."""
        return hash((self.x, self.y))
    
    def coast(self):
        """If the point is water (value 0) this method returns the number of 
        coast line around this point."""
        if self.value == "1":
            return 0
        return sum([int(p.value) for p in self.n()])



# Initialize total number of coast line
COAST = 0

# Initialize queue
q = set()

# Special case if the map is 1D (n or M = 1)
if N == M == 1:
    print(int(grid[0][0])*4)
elif N == 1 or M == 1:
    if M == 1:
        grid = [d[0] for d in grid]
    else: 
        grid = grid[0]
    for i, d in enumerate(grid):
        if d == "1":
            COAST += 2
            if i==0 or grid[i-1] == "0":
                COAST += 1
            if i == len(grid)-1:
                COAST += 1
        elif i > 0:
            if grid[i-1] == "1":
                COAST += 1
    print(COAST)
else: # Normal case (N and M >= 2)

    # Collect all point that line on the border and add the to the queue:
    for i in range(0, M):
        for p in [Point(0, i), Point(N-1, i)]:
            if p.value == "0":
                q.add(p)
            else: 
                if p.is_corner():
                    COAST += 2
                else: 
                    COAST += 1

    for i in range(1, N-1):
        for p in  [Point(i, 0), Point(i, M-1)]:
            if p.value == "0":
                q.add(p)
            else: 
                if p.is_corner():
                    COAST += 2
                else: 
                    COAST += 1
    

    # Initialize set of visited points
    seen = set()

    # While queue is not empty
    while q:
        p = q.pop()         # Pop one element from the queue
        COAST += p.coast()  # Count how much coast this point is sourounded by
        seen.add(p)         # Add to seen
        for n in p.n():     # Look at neighbors
            if n not in seen and n.value == "0":
                q.add(n)    # If neighbor is unvisited and water, add it to q

        

    print(COAST)