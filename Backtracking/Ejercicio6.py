"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: N-Reinas
Fecha: miércoles 19 de julio del 2023
""" 
def n_reinas(n):
    def es_seguro(fila, columna):
        for i in range(fila):
            if tablero[i] == columna or abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def backtrack(fila):
        if fila == n:
            soluciones.append(tablero[:])
            return
        for columna in range(n):
            if es_seguro(fila, columna):
                tablero[fila] = columna
                backtrack(fila + 1)

    soluciones = []
    tablero = [-1] * n
    backtrack(0)
    return soluciones
if __name__ == "__main__":
    n = 4
    soluciones = n_reinas(n)
    print(f"Soluciones para {n} reinas en un tablero de {n}x{n}:")
    for solucion in soluciones:
        print(solucion)
