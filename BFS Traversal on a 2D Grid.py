import random
from collections import deque

def create_grid(n):
    """Create N x N grid with random obstacles"""
    grid = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.random() < 0.25:  # 25% chance of obstacle
                grid[i][j] = 'X'
    return grid


def print_grid(grid, start=None, goal=None):
    """Print the grid with optional start and goal markers"""
    n = len(grid)
    display_grid = [row[:] for row in grid]

    if start:
        display_grid[start[0]][start[1]] = 'S'
    if goal:
        display_grid[goal[0]][goal[1]] = 'G'

    print("\nGrid Layout:")
    for i in range(n):
        for j in range(n):
            print(display_grid[i][j], end=' ')
        print()
    print()


def bfs_traversal(grid, start, goal):
    """Perform BFS traversal and print moves"""
    n = len(grid)
    directions = [(-1, 0, "Up"), (0, 1, "Right"), (1, 0, "Down"), (0, -1, "Left")]
    visited = [[False for _ in range(n)] for _ in range(n)]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    print("BFS Traversal Moves:")
    print("-" * 25)

    while queue:
        current_row, current_col = queue.popleft()
        print(f"At position: ({current_row}, {current_col})")

        if (current_row, current_col) == goal:
            print(f"\nGoal reached at ({goal[0]}, {goal[1]})! 🎯")
            return True

        for dr, dc, move_name in directions:
            new_row = current_row + dr
            new_col = current_col + dc

            if (0 <= new_row < n and 0 <= new_col < n and
                grid[new_row][new_col] != 'X' and
                not visited[new_row][new_col]):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
                print(f"Moving {move_name} -> ({new_row}, {new_col})")

    print("\nGoal cannot be reached! ❌")
    return False


def main():
    print("\n=== BFS Traversal on 2D Grid ===\n")
    n = int(input("Enter grid size N: "))

    grid = create_grid(n)
    print_grid(grid)

    print("Enter start position:")
    start_row = int(input("Start row: "))
    start_col = int(input("Start column: "))
    start = (start_row, start_col)

    print("\nEnter goal position:")
    goal_row = int(input("Goal row: "))
    goal_col = int(input("Goal column: "))
    goal = (goal_row, goal_col)

    if grid[start_row][start_col] == 'X':
        print("Error: Start position is an obstacle!")
        return
    if grid[goal_row][goal_col] == 'X':
        print("Error: Goal position is an obstacle!")
        return

    print_grid(grid, start, goal)
    bfs_traversal(grid, start, goal)


if __name__ == "__main__":
    main()
