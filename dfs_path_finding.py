import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()

def dfs_path(grid, x, y, goal, visited, path):
    n = len(grid)
    if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] == 1 or visited[x][y]:
        return False

    visited[x][y] = True
    path.append((x, y))

    if (x, y) == goal:
        return True

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for dx, dy in directions:
        if dfs_path(grid, x+dx, y+dy, goal, visited, path):
            return True

    path.pop()
    return False


# Main
n = int(input("Enter grid size N: "))
grid = [[0 if random.random() > 0.3 else 1 for _ in range(n)] for _ in range(n)]

print("\nGenerated Grid (0 = free, 1 = obstacle):")
print_grid(grid)

start_x, start_y = map(int, input("Enter start cell (row col): ").split())
goal_x, goal_y = map(int, input("Enter goal cell (row col): ").split())

visited = [[False]*n for _ in range(n)]
path = []

if dfs_path(grid, start_x, start_y, (goal_x, goal_y), visited, path):
    print("\nPath found from start to goal:")
    print(path)
else:
    print("\nNo path found (obstacles may block the way).")
