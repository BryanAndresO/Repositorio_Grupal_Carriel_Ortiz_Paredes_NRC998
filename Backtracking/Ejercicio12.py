def subconjuntos_de_tamano_k(nums, k):
    def backtrack(start, current_subset):
        # Si el subconjunto actual tiene el tamaño k, lo agregamos a la lista de resultados
        if len(current_subset) == k:
            resultados.append(list(current_subset))
            return

        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    resultados = []
    backtrack(0, [])
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 2
    subconjuntos_k = subconjuntos_de_tamano_k(nums, k)
    print(f"Subconjuntos de tamaño {k}:")
    for subconjunto in subconjuntos_k:
        print(subconjunto)
