import time

def exchange_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
# Número de repeticiones para obtener el promedio
num_repetitions = 100

total_execution_time = 0

for _ in range(num_repetitions):
    # Medir tiempo de ejecución
    start_time = time.time()
    exchange_sort(array)
    end_time = time.time()

    # Calcular tiempo transcurrido en milisegundos
    execution_time = (end_time - start_time) * 1000
    total_execution_time += execution_time

# Calcular promedio del tiempo de ejecución
average_execution_time = total_execution_time / num_repetitions

print("Array ordenado:")
print(array)
print("Tiempo de ejecución promedio: {:.3f} milisegundos".format(average_execution_time))
