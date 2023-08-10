import random  
import time  

def bubble_sort(arr):  

    n = len(arr)  

    for i in range(n):  

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1]:  

                arr[j], arr[j+1] = arr[j+1], arr[j] 

def quick_sort(arr): 

    if len(arr) <= 1: 

        return arr  

    pivot = arr[len(arr) // 2]  

    left = [x for x in arr if x < pivot]  

    middle = [x for x in arr if x == pivot]  

    right = [x for x in arr if x > pivot]  

    return quick_sort(left) + middle + quick_sort(right) 

# Generar una lista de 100 números aleatorios 
random_list = [random.randint(1, 1000) for _ in range(100)]
# Medir el tiempo de ejecución de Bubble Sort 
start_time = time.time()
bubble_sort(random_list.copy()) 
bubble_time = time.time()- start_time 
# Medir el tiempo de ejecución de Quick Sort 
start_time = time.time() 
quick_sort(random_list.copy()) 
quick_time = time.time()- start_time 
print(f"Tiempo de ejecución de Bubble Sort: {bubble_time} segundos") 
print(f"Tiempo de ejecución de Quick Sort: {quick_time} segundos") 