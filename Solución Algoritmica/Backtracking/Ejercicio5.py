def actividades_no_superpuestas(actividades):
    def es_valido(solucion_parcial):
        for i in range(len(solucion_parcial)):
            for j in range(i + 1, len(solucion_parcial)):
                inicio_i, fin_i = actividades[solucion_parcial[i]]
                inicio_j, fin_j = actividades[solucion_parcial[j]]
                if (inicio_i <= inicio_j < fin_i) or (inicio_j <= inicio_i < fin_j):
                    return False
        return True

    def backtrack(solucion_parcial, indice):
        nonlocal mejor_solucion
        if indice == len(actividades):
            if len(solucion_parcial) > len(mejor_solucion):
                mejor_solucion = solucion_parcial
            return

        # No incluir la actividad actual
        backtrack(solucion_parcial, indice + 1)

        # Incluir la actividad actual si es válida
        if es_valido(solucion_parcial + [indice]):
            backtrack(solucion_parcial + [indice], indice + 1)

    mejor_solucion = []
    backtrack([], 0)

    # Recuperar las actividades correspondientes a los índices de la mejor solución
    actividades_seleccionadas = [actividades[i] for i in mejor_solucion]
    return actividades_seleccionadas

# Ejemplo de uso
actividades = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
resultado = actividades_no_superpuestas(actividades)
print("Máxima cantidad de actividades no superpuestas:", len(resultado))
print("Actividades seleccionadas:", resultado)
