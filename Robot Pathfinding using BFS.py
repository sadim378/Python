from collections import deque
import random

def create_grid(rows, cols, start, goal):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.3 and (i, j) != start and (i, j) != goal:
                grid[i][j] = 'X'
    return grid

def print_grid(grid, path=[], start=None, goal=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print('S', end=' ')
            elif (i, j) == goal:
                print('G', end=' ')
            elif (i, j) in path:
                print('*', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return parent

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] != 'X':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

    return None  

def get_path(parent, goal):
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current[0]][current[1]]
    return path[::-1]

print("=== BFS Pathfinding ===")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

start_x = int(input("Enter start row: "))
start_y = int(input("Enter start column: "))
start = (start_x, start_y)

goal_x = int(input("Enter goal row: "))
goal_y = int(input("Enter goal column: "))
goal = (goal_x, goal_y)

grid = create_grid(rows, cols, start, goal)
print("\nGenerated Grid:")
print_grid(grid, start=start, goal=goal)

parent = bfs(grid, start, goal)

if parent:
    path = get_path(parent, goal)
    print("\nPath Found:\n")
    print_grid(grid, path=path, start=start, goal=goal)

    print("\nMoves:")
    for i in range(1, len(path)):
        px, py = path[i - 1]
        cx, cy = path[i]
        if cx > px:
            print(f"Down → ({cx},{cy})")
        elif cx < px:
            print(f"Up → ({cx},{cy})")
        elif cy > py:
            print(f"Right → ({cx},{cy})")
        else:
            print(f"Left → ({cx},{cy})")

    print(f"\nTotal Moves: {len(path) - 1}")
else:
    print("\nNo path found!")
