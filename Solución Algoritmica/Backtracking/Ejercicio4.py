def is_valid_move(maze, x, y):
    rows = len(maze)
    cols = len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

def solve_maze_backtracking(maze):
    def backtrack(x, y, path):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            solutions.append(path)
            return
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, new_x, new_y):
                maze[new_x][new_y] = -1  # Mark the cell as visited
                backtrack(new_x, new_y, path + [(new_x, new_y)])
                maze[new_x][new_y] = 0   # Backtrack: unmark the cell

    start_x, start_y = 0, 0
    solutions = []
    backtrack(start_x, start_y, [(start_x, start_y)])
    return solutions

# Ejemplo de uso:
maze_example = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0]
]

solutions = solve_maze_backtracking(maze_example)
for i, solution in enumerate(solutions):
    print(f"Solución {i + 1}: {solution}")
