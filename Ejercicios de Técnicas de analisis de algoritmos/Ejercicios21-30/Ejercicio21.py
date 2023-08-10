def coin_combinations(coins, target):
    def backtrack(remaining, current_combination):
        if remaining == 0:
            combinations.append(current_combination[:])
            return
        if remaining < 0:
            return
        for coin in coins:
            current_combination.append(coin)
            backtrack(remaining - coin, current_combination)
            current_combination.pop()

    combinations = []
    backtrack(target, [])
    return combinations

# Ejemplo de uso
coins = [1, 2, 5]
target = 5
result = coin_combinations(coins, target)
print("Combinaciones posibles de monedas:", result)
