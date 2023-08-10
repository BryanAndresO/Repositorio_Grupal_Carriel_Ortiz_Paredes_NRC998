def max_subarray_divide_and_conquer(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = max_subarray_divide_and_conquer(arr, low, mid)
    right_max = max_subarray_divide_and_conquer(arr, mid + 1, high)
    cross_max = max_crossing_subarray(arr, low, mid, high)

    return max(left_max, right_max, cross_max)

def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0

    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0

    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum

# Ejemplo de uso
arr = [2, -4, 6, 8, -10, 100, -6, 5]
result = max_subarray_divide_and_conquer(arr, 0, len(arr) - 1)
print("Suma máxima del subarreglo:", result)
