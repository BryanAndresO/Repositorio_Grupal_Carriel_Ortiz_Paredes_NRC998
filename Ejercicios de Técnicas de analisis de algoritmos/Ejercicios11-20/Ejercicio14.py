def linear_search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return i, j
    return -1, -1

def binary_search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid // cols][mid % cols]
        if num == target:
            return mid // cols, mid % cols
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, -1

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target_value = 5

linear_search_result = linear_search_matrix(matrix, target_value)
binary_search_result = binary_search_matrix(matrix, target_value)

print(f"Búsqueda lineal: {linear_search_result}")
print(f"Búsqueda binaria: {binary_search_result}")
