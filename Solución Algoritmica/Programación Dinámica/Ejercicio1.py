def mochila_01_programacion_dinamica(valores, pesos, capacidad_mochila):
    n = len(valores)
    dp = [[0 for _ in range(capacidad_mochila + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for capacidad_actual in range(1, capacidad_mochila + 1):
            if pesos[i - 1] <= capacidad_actual:
                dp[i][capacidad_actual] = max(dp[i - 1][capacidad_actual],
                                              valores[i - 1] + dp[i - 1][capacidad_actual - pesos[i - 1]])
            else:
                dp[i][capacidad_actual] = dp[i - 1][capacidad_actual]

    # Reconstruir la solución óptima
    capacidad_actual = capacidad_mochila
    elementos_seleccionados = []
    for i in range(n, 0, -1):
        if dp[i][capacidad_actual] != dp[i - 1][capacidad_actual]:
            elementos_seleccionados.append(i - 1)
            capacidad_actual -= pesos[i - 1]

    elementos_seleccionados.reverse()

    return dp[n][capacidad_mochila], elementos_seleccionados

# Ejemplo de uso:
valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad_mochila = 50

max_valor, elementos_seleccionados = mochila_01_programacion_dinamica(valores, pesos, capacidad_mochila)
print("Valor máximo:", max_valor)
print("Elementos seleccionados:", elementos_seleccionados)
