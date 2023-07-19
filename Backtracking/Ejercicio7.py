"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Tema: Suma de Subconjuntos con Resstricción
Fecha: miércoles 19 de julio del 2023
""" 
def encontrar_subconjuntos_en_rango(nums, rango_objetivo):
    def backtrack(inicio, suma_actual, subconjunto_actual):
        if rango_objetivo[0] <= suma_actual <= rango_objetivo[1]:
            subconjuntos.append(subconjunto_actual[:])
        if suma_actual > rango_objetivo[1]:
            return
        for i in range(inicio, len(nums)):
            subconjunto_actual.append(nums[i])
            backtrack(i + 1, suma_actual + nums[i], subconjunto_actual)
            subconjunto_actual.pop()

    subconjuntos = []
    nums.sort()
    backtrack(0, 0, [])
    return subconjuntos
if __name__ == "__main__":
    nums = [3, 1, 4, 2, 5]
    rango_objetivo = (5, 10)
    resultado = encontrar_subconjuntos_en_rango(nums, rango_objetivo)
    print("Subconjuntos con suma dentro del rango", rango_objetivo, ":")
    print(resultado)
