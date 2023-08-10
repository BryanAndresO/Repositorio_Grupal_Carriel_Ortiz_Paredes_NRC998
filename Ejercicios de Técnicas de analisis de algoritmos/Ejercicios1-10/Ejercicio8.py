def greedy_coin_change(coins, target_amount):
    coins.sort(reverse=True)
    coin_count = 0
    remaining_amount = target_amount

    for coin in coins:
        while remaining_amount >= coin:
            coin_count += 1
            remaining_amount -= coin

    return coin_count

# Ejemplo de uso
coin_values = [1, 5, 10, 25]
target_amount = 63

result = greedy_coin_change(coin_values, target_amount)
print(f"Número de monedas requeridas: {result}")
