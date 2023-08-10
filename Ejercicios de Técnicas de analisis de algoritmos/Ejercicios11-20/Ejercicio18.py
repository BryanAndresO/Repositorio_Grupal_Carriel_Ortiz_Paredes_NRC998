class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

# Ejemplo de uso
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

visited = [False] * g.vertices

import time

start_time = time.time()
g.dfs(0, visited)
end_time = time.time()

print(f"Tiempo de ejecución de DFS: {end_time - start_time} segundos")
