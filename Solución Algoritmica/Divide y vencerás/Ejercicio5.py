import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivote = random.choice(arr)
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    if k <= len(menores):
        return quickselect(menores, k)
    elif k <= len(menores) + len(iguales):
        return pivote
    else:
        return quickselect(mayores, k - len(menores) - len(iguales))

# Ejemplo de uso:
arreglo = [12, 3, 6, 8, 7, 10, 9]
k_esimo_mas_pequeno = quickselect(arreglo, 3)
print("Elemento k-ésimo más pequeño:", k_esimo_mas_pequeno)
