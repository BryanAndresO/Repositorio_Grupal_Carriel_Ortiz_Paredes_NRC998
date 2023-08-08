import math

def f(n):
    return 3 * n ** 2 + 2 * n + 1

def g(n):
    return 5 * n * math.log(n, 2) + 10

def encontrar_notacion_asintotica(f, g):
    if f == g:
        return "Θ(" + str(f) + ")"

    if f < g:
        return "O(" + str(g) + ")"

    if f > g:
        return "Ω(" + str(g) + ")"

valores_n = [10, 100, 1000, 10000]

for n in valores_n:
    valor_f = f(n)
    valor_g = g(n)
    
    notacion = encontrar_notacion_asintotica(valor_f, valor_g)
    
    print(f"Para n = {n}:")
    print(f"f(n) = {valor_f}")
    print(f"g(n) = {valor_g}")
    print(f"Notación asintótica: {notacion}\n")
