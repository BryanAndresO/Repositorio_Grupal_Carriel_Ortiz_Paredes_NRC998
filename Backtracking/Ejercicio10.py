def encontrar_subconjuntos_con_productos_multiples(nums, objetivo):
    def backtrack(inicio, producto_actual, subconjunto_actual):
        # Si el producto actual es múltiplo del objetivo, agregamos el subconjunto a la lista de resultados
        if producto_actual % objetivo == 0:
            resultados.append(list(subconjunto_actual))

        for i in range(inicio, len(nums)):
            # Si el número actual es igual a 1, no afectará el producto, por lo que lo omitimos
            if nums[i] == 1:
                continue

            # Si el producto actual es divisible por el número actual, seguimos con la recursión
            if producto_actual % nums[i] == 0:
                subconjunto_actual.append(nums[i])
                backtrack(i + 1, producto_actual * nums[i], subconjunto_actual)
                subconjunto_actual.pop()

    resultados = []
    nums.sort()  # Ordenamos los números para evitar duplicados en el resultado
    backtrack(0, 1, [])  # Llamamos a la función de backtracking con el producto inicial como 1
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    objetivo = 4
    subconjuntos_con_productos_multiples = encontrar_subconjuntos_con_productos_multiples(nums, objetivo)
    print("Subconjuntos cuyo producto es múltiplo de", objetivo, ":")
    for subconjunto in subconjuntos_con_productos_multiples:
        print(subconjunto)
