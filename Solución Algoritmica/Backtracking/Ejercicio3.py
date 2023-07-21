def combinaciones_backtracking(conjunto, tamano, inicio=0, combinacion_actual=[]):
    if len(combinacion_actual) == tamano:
        print(combinacion_actual)
        return

    for i in range(inicio, len(conjunto)):
        combinacion_actual.append(conjunto[i])
        combinaciones_backtracking(conjunto, tamano, i + 1, combinacion_actual)
        combinacion_actual.pop()

# Ejemplo de uso:
conjunto = [1, 2, 3, 4]
tamano_subconjunto = 2

print(f"Combinaciones de tamaño {tamano_subconjunto}:")
combinaciones_backtracking(conjunto, tamano_subconjunto)
