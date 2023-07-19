"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Subconjuntos con Suma Exacta
Fecha: miércoles 19 de julio del 2023
""" 
def encontrar_subconjuntos_con_suma_exacta(nums, suma_objetivo):
    def backtrack(inicio, objetivo, subconjunto_actual):
        if objetivo == 0:
            subconjuntos.append(subconjunto_actual[:])
            return
        for i in range(inicio, len(nums)):
            if objetivo - nums[i] >= 0:
                subconjunto_actual.append(nums[i])
                backtrack(i + 1, objetivo - nums[i], subconjunto_actual)
                subconjunto_actual.pop()

    subconjuntos = []
    nums.sort()
    backtrack(0, suma_objetivo, [])
    return subconjuntos
if __name__ == "__main__":
    nums = [3, 1, 4, 2, 5]
    suma_objetivo = 7
    resultado = encontrar_subconjuntos_con_suma_exacta(nums, suma_objetivo)
    print("Subconjuntos con suma igual a", suma_objetivo, ":")
    print(resultado)
