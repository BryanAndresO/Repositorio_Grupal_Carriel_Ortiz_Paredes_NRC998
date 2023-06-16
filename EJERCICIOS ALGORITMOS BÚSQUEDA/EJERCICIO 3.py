def busqueda_de_interpolacion(lista, objetivo):
    izquierda = 0  # Índice izquierdo del subarreglo de búsqueda
    derecha = len(lista) - 1  # Índice derecho del subarreglo de búsqueda
    while izquierda <= derecha and lista[izquierda] <= objetivo <= lista[derecha]:
        # Fórmula de interpolación para determinar la posición aproximada del objetivo
        posicion = izquierda + ((objetivo - lista[izquierda]) * (derecha - izquierda)) // (lista[derecha] - lista[izquierda])
        if lista[posicion] == objetivo:  # Si el número objetivo se encuentra en la posición encontrada
            return posicion  # Se retorna la posición del número objetivo
        if lista[posicion] < objetivo:  # Si el número objetivo es mayor que el valor en la posición encontrada
            izquierda = posicion + 1  # Se ajusta el índice izquierdo para buscar en el subarreglo derecho
        else:  # Si el número objetivo es menor que el valor en la posición encontrada
            derecha = posicion - 1  # Se ajusta el índice derecho para buscar en el subarreglo izquierdo
    return -1  # Si el número objetivo no se encuentra en la lista, se retorna -1

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numero_encontrar = int(input("Ingrese el número que desea buscar: "))
indice = busqueda_de_interpolacion(numeros, numero_encontrar)
if indice != -1:
    print(f"El número {numero_encontrar} se encuentra en la posición {indice}.")
else:
    print(f"El número {numero_encontrar} no se encuentra en la lista.")


