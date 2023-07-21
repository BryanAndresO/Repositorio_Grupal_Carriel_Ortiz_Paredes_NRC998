INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    # Inicializamos las distancias conocidas con los pesos de las aristas directas
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Aplicamos el algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Ejemplo de uso:
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

resultado = floyd_warshall(graph)
for fila in resultado:
    print(fila)
