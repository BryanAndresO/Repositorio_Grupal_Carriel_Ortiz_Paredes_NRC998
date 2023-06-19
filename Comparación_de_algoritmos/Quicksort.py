import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Arreglo de datos
print("Datos no ordenados")
data = [64, 34, 25, 12, 22, 11, 90]
print(data)
# Medir el tiempo de ejecución
start_time = time.time()
sorted_data = quicksort(data)
end_time = time.time()

# Calcular el tiempo de ejecución en milisegundos
execution_time = (end_time - start_time) * 1000

# Imprimir el resultado y el tiempo de ejecución en milisegundos
print("Conjunto de datos ordenado:")
print(sorted_data)
print("Tiempo de ejecución:", execution_time, "milisegundos")
