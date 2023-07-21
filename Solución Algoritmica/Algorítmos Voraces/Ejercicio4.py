def seleccion_actividades(actividades):
    actividades.sort(key=lambda x: x[1])  # Ordenar por hora de finalización ascendente
    seleccionadas = [actividades[0]]
    for i in range(1, len(actividades)):
        inicio_actual, fin_actual = actividades[i]
        inicio_ultima, fin_ultima = seleccionadas[-1]
        if inicio_actual >= fin_ultima:
            seleccionadas.append((inicio_actual, fin_actual))
    return seleccionadas

# Ejemplo de uso:
actividades = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
resultado = seleccion_actividades(actividades)
print("Actividades seleccionadas:", resultado)
