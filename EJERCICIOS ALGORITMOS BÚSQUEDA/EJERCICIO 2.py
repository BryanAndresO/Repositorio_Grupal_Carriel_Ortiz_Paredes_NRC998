#Integrantes: Carriel Pamela, Ortiz Bryan, Paredes Camila
#búsqueda binaria en una lista ordenada
#Solicitar al usuario un número objetivo y buscar ese número 
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Solicitar al usuario el número objetivo
numero_objetivo = int(input("Ingrese el número objetivo: "))

# Crear una lista de números enteros ordenada de forma ascendente
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Implementar la búsqueda binaria
posicion = busqueda_binaria(lista_numeros, numero_objetivo)

# Imprimir el resultado
if posicion != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"El número {numero_objetivo} no está presente en la lista.")
