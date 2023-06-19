import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2

# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
shell_sort(array)
print("Array ordenado:")
print(array)

# Medir el tiempo de ejecución en milisegundos
start_time = time.perf_counter()
shell_sort(array)
end_time = time.perf_counter()

print("Array ordenado:")
print(array)
print("Tiempo de ejecución:", (end_time - start_time) * 1000, "milisegundos")
