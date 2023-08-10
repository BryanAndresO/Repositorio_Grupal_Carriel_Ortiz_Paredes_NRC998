# Implementación de algoritmo de selección de actividades (Greedy)
def greedy_activity_selection(start, finish):
    activities = sorted(zip(finish, start))
    selected = [activities[0]]
    last_finish = activities[0][0]
    
    for activity in activities[1:]:
        if activity[1] >= last_finish:
            selected.append(activity)
            last_finish = activity[0]
    
    return selected

# Implementación del algoritmo de la mochila fraccional (Greedy)
def greedy_fractional_knapsack(weights, values, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    remaining_capacity = capacity
    selected_items = []

    for value, weight in items:
        if weight <= remaining_capacity:
            selected_items.append((weight, value))
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            selected_items.append((remaining_capacity, value * fraction))
            total_value += value * fraction
            break

    return total_value, selected_items

# Ejemplo de uso para comparar las notaciones asintóticas y resultados
activities_start = [1, 3, 0, 5, 8, 5]
activities_finish = [2, 4, 6, 7, 9, 9]
knapsack_weights = [10, 20, 30]
knapsack_values = [60, 100, 120]
knapsack_capacity = 50

selected_activities = greedy_activity_selection(activities_start, activities_finish)
knapsack_value, selected_items = greedy_fractional_knapsack(knapsack_weights, knapsack_values, knapsack_capacity)

print("Selección de actividades:", selected_activities)
print("Mochila fraccional - Valor total:", knapsack_value)
print("Mochila fraccional - Elementos seleccionados:", selected_items)
