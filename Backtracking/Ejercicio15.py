def combinaciones_con_suma_exacta(nums, objetivo):
    def backtrack(start, current_sum, current_combination):
        # Si la suma actual es igual al objetivo, agregamos la combinación actual a la lista de resultados
        if current_sum == objetivo:
            resultados.append(list(current_combination))
            return

        for i in range(start, len(nums)):
            # Si la suma actual excede el objetivo, no continuamos con este camino
            if current_sum + nums[i] > objetivo:
                continue

            current_combination.append(nums[i])
            backtrack(i, current_sum + nums[i], current_combination)
            current_combination.pop()

    resultados = []
    nums.sort()  # Ordenamos los números para evitar combinaciones duplicadas
    backtrack(0, 0, [])
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [2, 4, 6, 3, 5]
    objetivo = 10
    combinaciones = combinaciones_con_suma_exacta(nums, objetivo)
    print(f"Combinaciones que suman exactamente {objetivo}:")
    for combinacion in combinaciones:
        print(combinacion)
