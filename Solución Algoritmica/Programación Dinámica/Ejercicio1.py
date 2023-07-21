def longitud_subsecuencia_comun_mas_larga(cadena1, cadena2):
    m, n = len(cadena1), len(cadena2)

    # Creamos una matriz para almacenar los resultados intermedios
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Rellenamos la matriz utilizando el algoritmo de programación dinámica
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if cadena1[i - 1] == cadena2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # La longitud de la subsecuencia común más larga está almacenada en dp[m][n]
    return dp[m][n]

# Ejemplo de uso:
cadena1 = "ABCDGH"
cadena2 = "AEDFHR"
resultado = longitud_subsecuencia_comun_mas_larga(cadena1, cadena2)
print("Longitud de la subsecuencia común más larga:", resultado)
