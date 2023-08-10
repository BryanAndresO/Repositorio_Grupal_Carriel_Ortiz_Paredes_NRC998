def fractional_knapsack_greedy(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    remaining_capacity = capacity

    for weight, value in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break

    return total_value

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Ejemplo de uso
items = [(2, 40), (3, 50), (5, 100), (7, 80)]
knapsack_capacity = 10

greedy_result = fractional_knapsack_greedy(items, knapsack_capacity)
dynamic_result = knapsack_dynamic_programming([w for w, _ in items], [v for _, v in items], knapsack_capacity)

print(f"Algoritmo voraz: {greedy_result}")
print(f"Programación dinámica: {dynamic_result}")
