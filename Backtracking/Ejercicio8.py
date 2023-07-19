"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Permutaciones sin duplicados  
Fecha: miércoles 19 de julio del 2023
""" 
def permutaciones_sin_duplicados(nums):
    def backtrack(permutacion_actual):
        if len(permutacion_actual) == len(nums):
            permutaciones.append(permutacion_actual[:])
            return
        for num in nums:
            if num not in permutacion_actual:
                permutacion_actual.append(num)
                backtrack(permutacion_actual)
                permutacion_actual.pop()

    permutaciones = []
    backtrack([])
    return permutaciones
if __name__ == "__main__":
    nums = [1, 2, 3]
    resultado = permutaciones_sin_duplicados(nums)
    print("Permutaciones sin duplicados:")
    print(resultado)
