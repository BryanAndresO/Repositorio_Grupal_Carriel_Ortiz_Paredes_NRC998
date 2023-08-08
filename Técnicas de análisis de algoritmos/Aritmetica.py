def es_O(f_n, g_n):
    if g_n <= f_n:
        return True
    return False

def funcion_f1(n):
    return 3 * n ** 2 + 2 * n + 1

def funcion_f2(n):
    return 2 ** n

def funcion_g1(n):
    return 4 * n ** 2

def funcion_g2(n):
    return n ** 3

valores_n = [10, 100, 1000]

for n in valores_n:
    valor_f = funcion_f1(n)
    valor_g = funcion_g1(n)
    
    if es_O(valor_f, valor_g):
        relacion = "Sí"
    else:
        relacion = "No"
    
    print(f"Para n = {n}:")
    print(f"f(n) = {valor_f}")
    print(f"g(n) = {valor_g}")
    print(f"¿g(n) está en O(f(n))? {relacion}\n")
