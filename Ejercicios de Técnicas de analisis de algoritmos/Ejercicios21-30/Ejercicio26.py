def greedy_activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Ordenar actividades por tiempo de finalización
    selected_activities = [activities[0]]
    prev_activity = 0

    for i in range(1, len(activities)):
        if activities[i][0] >= activities[prev_activity][1]:
            selected_activities.append(activities[i])
            prev_activity = i

    return selected_activities

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    coin_count = 0
    i = 0

    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            coin_count += amount // coins[i]
            amount %= coins[i]
        i += 1

    return coin_count

# Ejemplo de uso para comparar las complejidades algorítmicas
activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9)]
selected = greedy_activity_selection(activities)
print("Actividades seleccionadas:", selected)

coins = [1, 5, 10, 25]
amount = 63
coin_count = greedy_coin_change(coins, amount)
print("Cantidad de monedas necesarias:", coin_count)
