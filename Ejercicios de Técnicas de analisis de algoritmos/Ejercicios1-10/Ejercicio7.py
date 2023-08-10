def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0

    for item in items:
        weight = item[0]
        value = item[1]
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (capacity / weight) * value
            break

    return total_value

# Ejemplo de uso
items = [(2, 40), (3, 50), (5, 100), (7, 80)]
knapsack_capacity = 10

max_value = fractional_knapsack(items, knapsack_capacity)
print(f"Valor máximo obtenido: {max_value}")
