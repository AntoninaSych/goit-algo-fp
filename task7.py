import random

def monte_carlo_simulation(num_trials):
    # Ініціалізуємо список для підрахунку кількості випадінь кожної суми
    sums_count = [0] * 11
    
    # Виконуємо симуляцію
    for _ in range(num_trials):
        # Кидаємо два кубики
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # Знаходимо суму чисел на кубиках і додаємо до списку sums_count
        sums_count[dice1 + dice2 - 2] += 1
    
    # Розраховуємо імовірності для кожної суми
    probabilities = [count / num_trials for count in sums_count]
    
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i}\t{prob:.2%} ({prob * 36:.0f}/36)")

# Кількість спроб для симуляції
num_trials = 100000

# Виконуємо симуляцію методом Монте-Карло
probabilities = monte_carlo_simulation(num_trials)

# Виводимо результати
print_probabilities(probabilities)
