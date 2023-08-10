def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Analizar la complejidad del algoritmo recursivo
# La recurrencia es T(n) = T(n-1) + O(1)
# Por lo tanto, la complejidad es O(n)
