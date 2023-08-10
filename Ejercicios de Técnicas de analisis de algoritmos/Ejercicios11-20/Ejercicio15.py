import time

def fibonacci_dynamic_programming(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Ejemplo de uso
n = 30

start_time = time.time()
fib_dynamic = fibonacci_dynamic_programming(n)
end_time = time.time()

print(f"Fibonacci programación dinámica({n}): {fib_dynamic}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
