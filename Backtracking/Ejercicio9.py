"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Combianciones de k Elementos
Fecha: miércoles 19 de julio del 2023
""" 
def combinaciones_k_elementos(nums, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            combinaciones.append(current_combination[:])
            return
        for i in range(start, len(nums)):
            current_combination.append(nums[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()

    combinaciones = []
    backtrack(0, [])
    return combinaciones
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 2
    resultado = combinaciones_k_elementos(nums, k)
    print(f"Combinaciones de {k} elementos:")
    print(resultado)
