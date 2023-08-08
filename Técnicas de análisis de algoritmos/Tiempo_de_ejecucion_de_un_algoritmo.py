import networkx as nx
import time

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def main():
    n = int(input("Ingrese el número de nodos: "))
    m = int(input("Ingrese el número de aristas: "))
    
    graph = nx.gnm_random_graph(n, m)
    visited = [False] * n
    
    start_time = time.time()
    
    for node in range(n):
        if not visited[node]:
            dfs(graph, node, visited)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Tiempo de ejecución: {execution_time:.11f} segundos")

if __name__ == "__main__":
    main()
