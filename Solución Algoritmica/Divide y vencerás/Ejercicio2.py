def encontrar_mayoritario(arr):
    candidato = None
    contador = 0

    for num in arr:
        if contador == 0:
            candidato = num
            contador = 1
        elif candidato == num:
            contador += 1
        else:
            contador -= 1

    # Verificar si el candidato es realmente mayoritario
    contador = arr.count(candidato)
    if contador > len(arr) / 2:
        return candidato
    else:
        return None

# Ejemplo de uso:
arreglo = [2, 2, 3, 2, 4, 2, 5, 2, 2]
mayoritario = encontrar_mayoritario(arreglo)
print("Elemento mayoritario:", mayoritario)
