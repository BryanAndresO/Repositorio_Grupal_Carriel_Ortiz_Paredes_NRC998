def solve_maze(maze):
    def backtrack(x, y):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return True
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
            return False

        maze[x][y] = 1  # Mark as visited
        if backtrack(x + 1, y) or backtrack(x - 1, y) or backtrack(x, y + 1) or backtrack(x, y - 1):
            return True
        maze[x][y] = 0  # Unmark if no path found
        return False

    return backtrack(0, 0)

# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

import time

start_time = time.time()
result = solve_maze(maze)
end_time = time.time()

print(f"Laberinto resuelto: {result}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
