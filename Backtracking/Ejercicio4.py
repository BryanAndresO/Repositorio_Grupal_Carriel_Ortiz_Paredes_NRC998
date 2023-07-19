"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Subconjuntos son Suma Exacta
Fecha: miércoles 19 de julio del 2023
"""
def Buscar_subconj_sumexact(num, Suma_objetivo):
    def backtrack(start, target, current_subset):
        if target == 0:
            subsets.append(current_subset[:])
            return
        for i in range(start, len(num)):
            if target - num[i] >= 0:
                current_subset.append(num[i])
                backtrack(i + 1, target - num[i], current_subset)
                current_subset.pop()

    subsets = []
    num.sort()
    backtrack(0, Suma_objetivo, [])
    return subsets

# Ejemplo de uso:
if __name__ == "__main__":
    nums = [3, 1, 4, 2, 5]
    target_sum = 7
    result = Buscar_subconj_sumexact(nums, target_sum)
    print("Subconjuntos con suma igual a", target_sum, ":")
    print(result)
