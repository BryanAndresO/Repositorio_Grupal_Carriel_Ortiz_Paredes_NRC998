def identify_notation_asymptotic(f):
    notation = "O(n^2)"  # Notación asintótica para función cuadrática (n^2)
    return notation

# Función de ejemplo f(n) = 3n^2 + 5n + 2
def f(n):
    return 3 * n ** 2 + 5 * n + 2

notation = identify_notation_asymptotic(f)
print("Notación Asintótica:", notation)
