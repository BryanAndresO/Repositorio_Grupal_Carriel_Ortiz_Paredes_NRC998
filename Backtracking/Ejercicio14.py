def subconjuntos_sin_duplicados(nums):
    def backtrack(start, current_subset):
        # Agregamos el subconjunto actual a la lista de resultados
        resultados.append(list(current_subset))

        for i in range(start, len(nums)):
            # Si el número actual es igual al número anterior, lo omitimos para evitar duplicados
            if i > start and nums[i] == nums[i - 1]:
                continue

            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    resultados = []
    nums.sort()  # Ordenamos los números para evitar duplicados en el resultado
    backtrack(0, [])
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 2, 2]
    subconjuntos = subconjuntos_sin_duplicados(nums)
    print("Subconjuntos sin duplicados:")
    for subconjunto in subconjuntos:
        print(subconjunto)
