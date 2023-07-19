"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Subconjuntos con Suma Exacta
Fecha: miércoles 19 de julio del 2023
""" 
def encontrar_combinaciones_con_suma_exacta(nums, suma_objetivo):
    def backtrack(inicio, suma_actual, combinacion_actual):
        if suma_actual == suma_objetivo:
            combinaciones.append(combinacion_actual[:])
            return
        for i in range(inicio, len(nums)):
            if suma_actual + nums[i] <= suma_objetivo:
                combinacion_actual.append(nums[i])
                backtrack(i, suma_actual + nums[i], combinacion_actual)
                combinacion_actual.pop()

    combinaciones = []
    nums.sort()
    backtrack(0, 0, [])
    return combinaciones
if __name__ == "__main__":
    nums = [2, 4, 6, 3]
    suma_objetivo = 6
    resultado = encontrar_combinaciones_con_suma_exacta(nums, suma_objetivo)
    print("Combinaciones con suma igual a", suma_objetivo, ":")
    print(resultado)
