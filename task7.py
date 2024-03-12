import random

def monte_carlo_simulation(num_trials):
    """
    Perform Monte Carlo simulation of rolling two dice for a large number of trials.
    Args:
    - num_trials (int): The number of trials to perform.

    Returns:
    - probabilities (list): List of probabilities for each possible sum.
    """
    sums = [0] * 11  # Initialize list to store the frequency of each possible sum (2-12)
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums[total - 2] += 1  # Increment the frequency of the corresponding sum
    probabilities = [count / num_trials * 100 for count in sums]  # Calculate probabilities in percentage
    return probabilities

# Perform Monte Carlo simulation with a large number of trials
num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

# Print probabilities for each possible sum
print("Sum\tProbability")
for i, prob in enumerate(probabilities, start=2):
    print(f"{i}\t{prob:.2f}% ({prob / 100 * num_trials}/{num_trials})")
