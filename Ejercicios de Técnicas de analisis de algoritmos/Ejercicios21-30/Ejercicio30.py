def find_max_min_divide_and_conquer(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    mid = (low + high) // 2

    left_max, left_min = find_max_min_divide_and_conquer(arr, low, mid)
    right_max, right_min = find_max_min_divide_and_conquer(arr, mid + 1, high)

    return max(left_max, right_max), min(left_min, right_min)

# Ejemplo de uso para analizar la complejidad algorítmica
arr = [2, -4, 6, 8, -10, 100, -6, 5]
max_value, min_value = find_max_min_divide_and_conquer(arr, 0, len(arr) - 1)
print("Valor máximo del arreglo:", max_value)
print("Valor mínimo del arreglo:", min_value)
