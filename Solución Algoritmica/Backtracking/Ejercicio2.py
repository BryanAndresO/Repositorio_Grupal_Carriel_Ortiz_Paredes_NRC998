def mochila_01_backtracking(valores, pesos, capacidad_mochila):
    def backtrack(indice, capacidad_actual, valor_actual, seleccionados):
        nonlocal max_valor, solucion_optima

        if capacidad_actual > capacidad_mochila:
            return

        if valor_actual > max_valor:
            max_valor = valor_actual
            solucion_optima = seleccionados.copy()

        if indice == len(valores):
            return

        # No seleccionar el elemento actual
        backtrack(indice + 1, capacidad_actual, valor_actual, seleccionados)

        # Seleccionar el elemento actual
        seleccionados.append(indice)
        backtrack(indice + 1, capacidad_actual + pesos[indice], valor_actual + valores[indice], seleccionados)
        seleccionados.pop()

    max_valor = 0
    solucion_optima = []
    backtrack(0, 0, 0, [])
    return max_valor, solucion_optima

# Ejemplo de uso:
valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad_mochila = 50

max_valor, solucion_optima = mochila_01_backtracking(valores, pesos, capacidad_mochila)
print("Valor máximo:", max_valor)
print("Elementos seleccionados:", solucion_optima)
