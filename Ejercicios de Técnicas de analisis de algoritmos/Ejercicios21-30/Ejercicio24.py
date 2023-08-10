def recursive_backtracking_sum(n):
    if n == 0:
        return 0
    return recursive_backtracking_sum(n - 1) + n

# Ejemplo de uso
n = 5
result = recursive_backtracking_sum(n)
print(f"Suma recursiva de los primeros {n} números naturales:", result)
