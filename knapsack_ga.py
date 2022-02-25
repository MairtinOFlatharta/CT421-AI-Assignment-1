#!/usr/bin/env python
import statistics
import matplotlib.pyplot as plt
from numpy.random import randint, rand, choice


# Values of all items
values = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457,
          1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277,
          2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257,
          369261]
# Weights of all items
weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150,
           823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111,
           323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]
# Maximum weight that knapsack can hold
W = 6404180
# Size of each chromosome population
population_size = 500
# Number of items and length of bitstrings
n_items = len(values)
# Chance of a chromosome mutating
mutation_rate = 0.5
# Chance of a crossover occuring between 2 parent chromosomes
crossover_rate = 0.9
# Total number of generations produced
total_iter = 10
# List of average fitness of each generation
averages = []
# List of best fitness of each generation
best_fitness = []
# Max value of a bit string in the population
max_value = (1 << n_items) - 1


def main():
    population = []

    # Generate initial generation of chromosomes
    for i in range(0, population_size):
        population.append(randint(0, max_value+1))

    results = genetic_algorithm(population)
    print(f'Best knapsack found: {results[0]:024b}')
    print(f'Best score: {results[1]}')
    plot_averages(averages, total_iter)


def genetic_algorithm(population):

    # Stores best overall knapsack
    best_knapsack = 0

    # Cycle through generations
    for gen in range(total_iter):
        parents = []
        children = []

        # Calculate all fitness scores for population
        scores = [fitness(x, values, weights, W) for x in population]

        averages.append(statistics.fmean(scores))

        # Print scores of current generation
        best_index, best_score = scores.index(max(scores)), max(scores)
        best_fitness.append(best_score)
        if best_score > fitness(best_knapsack, values, weights, W):
            best_knapsack = population[best_index]
        print(f'Generation {gen+1}')
        print(f'Best item: {population[best_index]:024b}')
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
    return best_knapsack, fitness(best_knapsack, values, weights, W)


def mutate(chrom):
    # Flip 1 random bit in the chromosome (if mutation is triggered)
    if rand() < mutation_rate:
        # Either remove or add item based on randomly chosen index value
        if rand() < 0.5:
            index = randint(0, n_items)
            return (chrom ^ (1 << index))
        else:
            # Replace item in knapsack with some other item

            # Generate list of indicies of items that are in knapsack
            taken = [x for x in range(n_items)
                     if ((chrom >> (n_items - x - 1)) & 1)]

            # Generate list of indicies of items that are not in knapsack
            not_taken = [x for x in range(n_items) if x not in taken]

            # Pick 1 random item to remove, and 1 random item to add
            item_to_remove = choice(taken)
            item_to_take = choice(not_taken)

            # Perform the item replacement
            chrom = (chrom ^ (1 << (n_items - item_to_remove - 1)))
            chrom = (chrom ^ (1 << (n_items - item_to_take - 1)))
    return chrom


def crossover(parent_1, parent_2):
    # Children are copies of their respective parents
    child_1, child_2 = parent_1, parent_2

    # Randomly decide if crossover happens based on crossover_rate
    if rand() < crossover_rate:
        # i is the index where the crossover will happen between parents
        i = randint(1, n_items-1)

        # front_mask captures first i bits of binary
        # back_mask captures the rest of the bits
        front_mask = ((1 << i) - 1) << (n_items - i)
        back_mask = (1 << (n_items - i)) - 1

        # child_1 is the first i bits of parent_1. The rest are from parent_2
        child_1 = (parent_1 & front_mask) | (parent_2 & back_mask)

        # child_2 is the first i bits of parent_2. The rest are from parent_1
        child_2 = (parent_2 & front_mask) | (parent_1 & back_mask)

    return child_1, child_2


def tournament_selection(population, scores, rounds=3):

    # Pick some random index in population
    best_chrom = randint(0, population_size)

    # Pick contending chromosomes randomly
    for chrom in randint(0, population_size, rounds-1):
        # Find best score in tournament round
        if scores[chrom] > scores[best_chrom]:
            best_chrom = chrom
    return population[best_chrom]


def fitness(chrom, values, weights, W):
    value_total = 0
    weight_total = 0
    for i in range(n_items):
        # Sum up total value and weight of all items in knapsack
        value_total += values[i] * ((chrom >> (n_items - i - 1)) & 1)
        weight_total += weights[i] * ((chrom >> (n_items - i - 1)) & 1)

    if weight_total <= W:
        # Weight is below threshold. Return total
        return value_total
    # Weight exceeded limit. Return extra weight as negative
    return (W - weight_total)


def plot_averages(averages, total_iter):
    plt.plot(range(1, total_iter+1), averages, marker='o',
             label='Average Fitness')
    plt.plot(range(1, total_iter+1), best_fitness, marker='o',
             label='Best Fitness')
    plt.legend(['Average Fitness', 'Best Fitness'])
    plt.ticklabel_format(style='plain')
    plt.title(f'Average fitness and best fitness over {total_iter} '
              'generations (Knapsack GA)')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
