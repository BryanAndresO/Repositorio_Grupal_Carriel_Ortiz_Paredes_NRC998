import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Comparar tiempos de ejecución para listas pequeñas
small_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

start_time = time.time()
linear_search(small_list, target)
end_time = time.time()
print("Tiempo de Búsqueda Lineal:", end_time - start_time, "segundos")

start_time = time.time()
binary_search(small_list, target)
end_time = time.time()
print("Tiempo de Búsqueda Binaria:", end_time - start_time, "segundos")
