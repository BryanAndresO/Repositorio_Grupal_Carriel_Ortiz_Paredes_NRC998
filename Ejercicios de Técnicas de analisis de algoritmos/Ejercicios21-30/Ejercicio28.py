def recursive_backtracking_analysis(n):
    if n == 0:
        return 0
    return recursive_backtracking_analysis(n - 1) + 1

# Ejemplo de uso para analizar la complejidad algorítmica
n = 5
result = recursive_backtracking_analysis(n)
print(f"Complejidad algorítmica de la recurrencia: T({n}) =", result)
