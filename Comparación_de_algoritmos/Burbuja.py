import time

def exchange_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
exchange_sort(array)
print("Array ordenado:")
print(array)

# Medir el tiempo de ejecución
start_time = time.time()
exchange_sort(array)
end_time = time.time()

print("Tiempo de ejecución:", end_time - start_time)
