def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
import random
import time

array = random.sample(range(1, 10001), 1000)

bubble_sort_array = array.copy()
start_time = time.time()
bubble_sort(bubble_sort_array)
end_time = time.time()
bubble_sort_time = end_time - start_time

quick_sort_array = array.copy()
start_time = time.time()
quick_sort(quick_sort_array)
end_time = time.time()
quick_sort_time = end_time - start_time

print(f"Tiempo de BubbleSort: {bubble_sort_time} segundos")
print(f"Tiempo de QuickSort: {quick_sort_time} segundos")
