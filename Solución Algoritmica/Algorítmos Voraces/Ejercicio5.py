import heapq

def dijkstra(grafo, inicio, fin):
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        dist_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if dist_actual > distancia[nodo_actual]:
            continue

        for vecino, peso_arista in grafo[nodo_actual].items():
            dist_total = dist_actual + peso_arista

            if dist_total < distancia[vecino]:
                distancia[vecino] = dist_total
                heapq.heappush(cola_prioridad, (dist_total, vecino))

    return distancia[fin]

# Ejemplo de uso:
grafo_ponderado_dirigido = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 3}
}

inicio = 'A'
fin = 'D'
distancia_minima = dijkstra(grafo_ponderado_dirigido, inicio, fin)
print(f"Distancia mínima entre {inicio} y {fin}: {distancia_minima}")

