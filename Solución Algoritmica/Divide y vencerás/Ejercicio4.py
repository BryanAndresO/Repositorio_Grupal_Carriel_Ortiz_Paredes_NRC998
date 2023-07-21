def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == elemento:
            return medio
        elif valor_medio < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None

# Ejemplo de uso:
lista_ordenada = [3, 6, 9, 12, 15, 18, 21, 24]
elemento_buscado = 15
indice_encontrado = busqueda_binaria(lista_ordenada, elemento_buscado)
print("Elemento encontrado en el índice:", indice_encontrado)
