import numpy as np

def multiplicacion_matrices(A, B):
    return np.dot(A, B)

# Ejemplo de uso:
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])
resultado = multiplicacion_matrices(matriz_A, matriz_B)
print("Resultado de la multiplicación de matrices:")
print(resultado)
