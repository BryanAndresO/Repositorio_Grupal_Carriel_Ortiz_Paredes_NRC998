def permutaciones_con_repeticion(nums):
    def backtrack(permutacion_actual):
        # Si la permutación actual tiene la misma longitud que el conjunto de números, la agregamos a la lista de resultados
        if len(permutacion_actual) == len(nums):
            resultados.append(list(permutacion_actual))
            return

        for num in nums:
            permutacion_actual.append(num)
            backtrack(permutacion_actual)
            permutacion_actual.pop()

    resultados = []
    backtrack([])
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 2, 2]
    permutaciones = permutaciones_con_repeticion(nums)
    print("Permutaciones con repetición:")
    for permutacion in permutaciones:
        print(permutacion)
