def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Analizar la complejidad del algoritmo recursivo de Fibonacci
# La recurrencia es T(n) = T(n-1) + T(n-2) + O(1)
# Por lo tanto, la complejidad es exponencial, O(2^n)
