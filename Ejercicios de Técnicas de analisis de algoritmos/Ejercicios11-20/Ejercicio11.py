import time

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    size = len(arr)
    i = 1
    while i < size and arr[i] <= target:
        i *= 2

    start_time = time.time()
    # Implementa aquí tu algoritmo de búsqueda exponencial en 'arr' para encontrar 'target'
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Ejemplo de uso
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

estimated_time = exponential_search(sorted_array, target_value)
print(f"Tiempo estimado de ejecución: {estimated_time} segundos")
