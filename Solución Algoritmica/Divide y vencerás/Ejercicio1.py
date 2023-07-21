def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    result = []
    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            result.append(izquierda[i])
            i += 1
        else:
            result.append(derecha[j])
            j += 1

    result.extend(izquierda[i:])
    result.extend(derecha[j:])
    return result

# Ejemplo de uso:
conjunto_numeros = [38, 27, 43, 3, 9, 82, 10]
resultado = merge_sort(conjunto_numeros)
print("Conjunto de números ordenado:", resultado)
