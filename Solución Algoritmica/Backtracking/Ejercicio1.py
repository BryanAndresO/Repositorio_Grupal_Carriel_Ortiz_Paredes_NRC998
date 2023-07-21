def es_seguro(tablero, fila, columna, n):
    # Verificar si no hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar si no hay otra reina en la misma diagonal izquierda hacia arriba
    i, j = fila - 1, columna - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar si no hay otra reina en la misma diagonal derecha hacia arriba
    i, j = fila - 1, columna + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def resolver_n_reinas(tablero, fila, n, soluciones):
    if fila == n:
        # Se encontró una solución válida, se agrega a la lista de soluciones
        solucion = ["".join("Q" if c == 1 else "." for c in fila) for fila in tablero]
        soluciones.append(solucion)
        return

    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[fila][columna] = 1
            resolver_n_reinas(tablero, fila + 1, n, soluciones)
            tablero[fila][columna] = 0

def n_reinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones)
    return soluciones

# Ejemplo de uso:
n = 4
soluciones_n_reinas = n_reinas(n)
for idx, solucion in enumerate(soluciones_n_reinas, 1):
    print(f"Solución {idx}:")
    for fila in solucion:
        print(fila)
    print()
