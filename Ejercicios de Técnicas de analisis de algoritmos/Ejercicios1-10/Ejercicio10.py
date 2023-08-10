def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dynamic_programming(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Ejemplo de uso
n = 10

# Comparación de eficiencia
import time

start_time = time.time()
fib_recursive = fibonacci_recursive(n)
end_time = time.time()
print(f"Fibonacci recursivo({n}): {fib_recursive}, Tiempo: {end_time - start_time} segundos")

start_time = time.time()
fib_dynamic = fibonacci_dynamic_programming(n)
end_time = time.time()
print(f"Fibonacci programación dinámica({n}): {fib_dynamic}, Tiempo: {end_time - start_time} segundos")

