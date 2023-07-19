def combinaciones_con_repeticion(nums, k):
    def backtrack(start, current_combination):
        # Si la combinación actual tiene k elementos, la agregamos a la lista de resultados
        if len(current_combination) == k:
            resultados.append(list(current_combination))
            return

        for i in range(start, len(nums)):
            current_combination.append(nums[i])
            backtrack(i, current_combination)  # Permitimos repeticiones, por lo que pasamos el mismo índice
            current_combination.pop()

    resultados = []
    backtrack(0, [])
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 2
    combinaciones_k = combinaciones_con_repeticion(nums, k)
    print(f"Combinaciones de {k} elementos con repetición:")
    for combinacion in combinaciones_k:
        print(combinacion)
