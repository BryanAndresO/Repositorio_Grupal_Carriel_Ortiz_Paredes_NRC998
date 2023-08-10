def funcion_g(n):
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += i + j
    return result

def funcion_n_log_n(n):
    return n * (n - 1) // 2  # Suma de los primeros (n - 1) números naturales

# Prueba de la función funcion_g
n = 5
resultado_g = funcion_g(n)
print(f"funcion_g({n}) = {resultado_g}")

# Prueba de la función funcion_n_log_n
resultado_n_log_n = funcion_n_log_n(n)
print(f"funcion_n_log_n({n}) = {resultado_n_log_n}")
