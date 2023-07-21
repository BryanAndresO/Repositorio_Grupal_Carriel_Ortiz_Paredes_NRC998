def subset_sum(nums, target_sum):
    n = len(nums)

    # Creamos una matriz para almacenar los resultados intermedios
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Inicializamos la primera columna como True porque una suma objetivo de 0 siempre es posible
    for i in range(n + 1):
        dp[i][0] = True

    # Rellenamos la matriz utilizando el enfoque de programación dinámica
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # El resultado estará en la celda dp[n][target_sum]
    return dp[n][target_sum]

# Ejemplo de uso:
conjunto = [3, 34, 4, 12, 5, 2]
suma_objetivo = 9
resultado = subset_sum(conjunto, suma_objetivo)

if resultado:
    print("Sí, existe un subconjunto con la suma objetivo.")
else:
    print("No existe un subconjunto con la suma objetivo.")
