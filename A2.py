import heapq

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm Implementation
def astar(start, goal, grid):
    # Directions to move in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f, g, position)
    
    # To keep track of the shortest path
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        # Get the node with the lowest f value
        _, current_g, current = heapq.heappop(open_list)
        
        # If we reach the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Explore neighbors
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check if neighbor is within bounds and not blocked (represented by 1)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 1:
                tentative_g_score = current_g + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
    
    return None  # No path found

# Predefined grid (0 = free space, 1 = blocked space)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Predefined start and goal positions
start = (0, 0)
goal = (4, 4)

# Run A* algorithm
path = astar(start, goal, grid)

# Print the result
if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
