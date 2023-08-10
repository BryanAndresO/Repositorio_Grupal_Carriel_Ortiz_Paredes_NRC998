def divide_and_conquer_recurrence(n):
    if n == 1:
        return 1
    else:
        return 2 * divide_and_conquer_recurrence(n // 2) + 1

# Ejemplo de uso
n = 16
result = divide_and_conquer_recurrence(n)
print(f"Resultado de la recurrencia T({n}) = {result}")
