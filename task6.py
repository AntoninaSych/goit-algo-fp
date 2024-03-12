def greedy_algorithm(items, budget):
    """
    Greedy algorithm to choose food items maximizing calories-to-cost ratio within the budget.
    Args:
    - items (dict): Dictionary containing food items with their cost and calories.
    - budget (int): The maximum budget available.

    Returns:
    - chosen_items (list): List of chosen food items.
    """
    items_list = list(items.items())
    sorted_items = sorted(items_list, key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen_items = []
    total_cost = 0
    for item_name, item in sorted_items:
        item_cost = item['cost']
        if total_cost + item_cost <= budget:
            chosen_items.append(item_name)
            total_cost += item_cost
        else:
            break
    
    return chosen_items

def dynamic_programming(items, budget):
    """
    Dynamic programming algorithm to choose food items maximizing calories within the budget.
    Args:
    - items (dict): Dictionary containing food items with their cost and calories.
    - budget (int): The maximum budget available.

    Returns:
    - chosen_items (list): List of chosen food items.
    """
    items_list = list(items.items())
    n = len(items_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        item_name, item = items_list[i - 1]
        for j in range(budget + 1):
            item_cost = item['cost']
            item_calories = item['calories']
            if item_cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)
            else:
                dp[i][j] = dp[i - 1][j]
    chosen_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, _ = items_list[i - 1]
            chosen_items.append(item_name)
            j -= items_list[i - 1][1]['cost']
    return chosen_items

# Example usage:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Greedy Algorithm
greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm result:", greedy_result)

# Dynamic Programming Algorithm
dp_result = dynamic_programming(items, budget)
print("Dynamic Programming result:", dp_result)
