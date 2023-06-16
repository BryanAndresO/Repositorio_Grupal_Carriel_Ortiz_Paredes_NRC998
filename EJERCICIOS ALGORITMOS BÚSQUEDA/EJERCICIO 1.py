def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en una lista de números enteros.
    Devuelve la posición del número objetivo si se encuentra en la lista.
    Devuelve -1 si el número objetivo no está presente en la lista.
    """
    for indice, elemento in enumerate(lista):  # Recorre la lista obteniendo el índice y el valor de cada elemento
        if elemento == objetivo:  # Compara cada elemento con el número objetivo
            return indice  # Devuelve la posición del número objetivo si se encuentra
    return -1  # Devuelve -1 si el número objetivo no está presente

numero_busqueda = int(input("Ingrese el número que quiere buscar: "))  # Solicita al usuario el número objetivo
lista = [6, 9, 12, 10, 13, 18, 20]  # Crea una lista de números enteros

posicion = busqueda_lineal(lista, numero_busqueda)  # Realiza la búsqueda lineal en la lista

if posicion != -1:  # Si la posición es diferente de -1, el número objetivo se encontró en la lista
    print("El número", numero_busqueda, "se encuentra en la posición", posicion)
else:
    print("El número", numero_busqueda, "no está en la lista.")
