import time

def search_algorithm(arr, target):
    start_time = time.time()
    # Implementa aquí tu algoritmo de búsqueda en 'arr' para encontrar 'target'
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Ejemplo de uso
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

estimated_time = search_algorithm(array, target_value)
print(f"Tiempo estimado de ejecución: {estimated_time} segundos")
