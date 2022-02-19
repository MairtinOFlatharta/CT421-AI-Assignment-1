#!/usr/bin/env python
import statistics
import string
import matplotlib.pyplot as plt
from numpy.random import randint, rand, choice


# Size of each chromosome population
population_size = 100
# Length of number strings
digits = 30
# Chance of a chromosome mutating
mutation_rate = 0.5
# Chance of a crossover occuring between 2 parent chromosomes
crossover_rate = 0.9
# Total number of generations produced
total_iter = 50
# Current char set being used (0 - 9)
char_set = list(string.digits)
# List of average fitness of each generation
averages = []
# Target value is random int with specified number of digits
target = ''.join(choice(char_set) for _ in range(digits))


def main():
    print(f'Target string is: {target}\n')
    population = []

    # Generate initial generation of chromosomes
    for i in range(0, population_size):
        population.append(''.join(choice(char_set) for _ in range(digits)))

    genetic_algorithm(population)
    plot_averages(averages, total_iter)


def genetic_algorithm(population):

    # Cycle through generations
    for gen in range(total_iter):
        parents = []
        children = []

        # Calculate all fitness scores for population
        scores = [fitness(x, target) for x in population]

        averages.append(statistics.fmean(scores))

        # Print scores of current generation
        best_index, best_score = scores.index(max(scores)), max(scores)
        print(f'Generation {gen+1}')
        print(f'Best item: {population[best_index]}')
        print(f'Item score: {best_score}')
        print(f'Generation average score: {averages[gen]}\n')

        # Find parent chromosomes of next generation via selection
        for i in range(population_size):
            parents.append(tournament_selection(population, scores))

        # Pair up chromosome with the one right after it
        for i in range(0, population_size, 2):
            parent_1, parent_2 = parents[i], parents[i+1]

            # Perform crossover, mutate children and append to list
            for child in crossover(parent_1, parent_2):
                child = mutate(child)
                children.append(child)

        # Replace current generation with children
        population = children


def mutate(chrom):
    # Increment or decrement 1 random digit of chromosome
    # (if mutation is triggered)
    if rand() < mutation_rate:
        index = randint(0, digits)

        # Get digit at chosen index
        original_digit = int(chrom[index])

        # 50/50 chance of incrementing or decrementing
        if rand() <= 0.5:
            # Incrementing
            if original_digit == 9:
                # Digit is 9. Overflow it back to 0
                new_digit = 0
            else:
                new_digit = original_digit + 1
        else:
            # Decrementing
            if original_digit == 0:
                # Digit is 0. Underflow it back to 9
                new_digit = 0
            else:
                new_digit = original_digit - 1
        return (chrom[:index] + str(new_digit) + chrom[index+1:])

    return chrom


def crossover(parent_1, parent_2):
    # Children are copies of their respective parents
    child_1, child_2 = parent_1, parent_2

    # Randomly decide if crossover happens based on crossover_rate
    if rand() < crossover_rate:
        # i is the index where the crossover will happen between parents
        i = randint(1, digits-1)

        # child_1 is the first i digits of parent_1
        # The rest are from parent_2
        child_1 = (parent_1[:i] + parent_2[i:])

        # child_2 is the first i digits of parent_2
        # The rest are from parent_1
        child_2 = (parent_2[:i] + parent_1[i:])

    return child_1, child_2


def tournament_selection(population, scores, rounds=5):

    # Pick some random index in population
    best_chrom = randint(0, population_size)

    # Pick contending chromosomes randomly
    for chrom in randint(0, population_size, rounds-1):
        # Find best score in tournament round
        if scores[chrom] > scores[best_chrom]:
            best_chrom = chrom
    return population[best_chrom]


def fitness(chrom, target):
    current_score = 0.0
    # Difference between target digit and chrom digit
    diff = 0
    # Fitness penalty for how far off chrom digit is from target digit
    fitness_penalty = 0.2
    for i in range(digits):
        # Cycle through all digits of chrom and target
        # Based on how different digits are distance-wise, get fitness
        diff = get_smallest_difference(int(chrom[i]), int(target[i]))
        current_score += 1 - (fitness_penalty * diff)
    return current_score


def get_smallest_difference(num1, num2):
    diffs = []
    diffs.append(abs(num1 - num2))
    diffs.append((num1 + 10) - num2)
    diffs.append(abs(num1 - (num2 + 10)))
    return min(diffs)


def plot_averages(averages, total_iter):
    plt.plot(range(1, total_iter+1), averages)
    plt.title(f'Average fitness over {total_iter} '
              'generations (Digit Target String)')
    plt.xlabel('Generation')
    plt.ylabel('Average fitness')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
