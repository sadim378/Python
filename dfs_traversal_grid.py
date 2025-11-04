import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()

def dfs_traversal(grid, x, y, visited):
    n = len(grid)
    if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] == 1 or visited[x][y]:
        return

    visited[x][y] = True
    print(f"Visited: ({x}, {y})")

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for dx, dy in directions:
        dfs_traversal(grid, x+dx, y+dy, visited)


# Main
n = int(input("Enter grid size N: "))
grid = [[0 if random.random() > 0.3 else 1 for _ in range(n)] for _ in range(n)]

print("\nGenerated Grid (0 = free, 1 = obstacle):")
print_grid(grid)

start_x, start_y = map(int, input("Enter start cell (row col): ").split())
goal_x, goal_y = map(int, input("Enter goal cell (row col): ").split())

visited = [[False]*n for _ in range(n)]
print("\nDFS Traversal Order:")
dfs_traversal(grid, start_x, start_y, visited)
