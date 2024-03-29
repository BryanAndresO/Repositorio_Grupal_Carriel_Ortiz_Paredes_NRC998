def longest_common_subsequence_length(str1, str2):
    m, n = len(str1), len(str2)

    # Creamos una matriz para almacenar los resultados intermedios
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Rellenamos la matriz utilizando el algoritmo de programación dinámica
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # La longitud de la subsecuencia común más larga está almacenada en dp[m][n]
    return dp[m][n]

# Ejemplo de uso:
cadena1 = "ABCDGH"
cadena2 = "AEDFHR"
resultado = longest_common_subsequence_length(cadena1, cadena2)
print("Longitud de la subsecuencia común más larga:", resultado)
