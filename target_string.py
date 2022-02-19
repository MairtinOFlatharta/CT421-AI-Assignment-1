#!/usr/bin/env python
import statistics
import matplotlib.pyplot as plt
from numpy.random import randint, rand


# Size of each chromosome population
population_size = 100
# Length of bitstrings
bits = 30
# Chance of a chromosome mutating
mutation_rate = 0.5
# Chance of a crossover occuring between 2 parent chromosomes
crossover_rate = 0.9
# Total number of generations produced
total_iter = 10
# List of average fitness of each generation
averages = []
# Max value of a bit string in the population
max_value = (1 << bits) - 1
# Target of GA is a random 30 bit string
target = randint(0, max_value)


def main():
    print(f'Target string is: {target:030b}\n')
    population = []

    # Generate initial generation of chromosomes
    for i in range(0, population_size):
        population.append(randint(0, max_value+1))

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
        print(f'Best item: {population[best_index]:030b}')
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
    # Flip 1 random bit in the chromosome (if mutation is triggered)
    if rand() < mutation_rate:
        index = randint(0, bits)
        return (chrom ^ (1 << index))
    return chrom


def crossover(parent_1, parent_2):
    # Children are copies of their respective parents
    child_1, child_2 = parent_1, parent_2

    # Randomly decide if crossover happens based on crossover_rate
    if rand() < crossover_rate:
        # i is the index where the crossover will happen between parents
        i = randint(1, bits-1)

        # front_mask captures first i bits of binary
        # back_mask captures the rest of the bits
        front_mask = ((1 << i) - 1) << (bits - i)
        back_mask = (1 << (bits - i)) - 1

        # child_1 is the first i bits of parent_1. The rest are from parent_2
        child_1 = (parent_1 & front_mask) | (parent_2 & back_mask)

        # child_2 is the first i bits of parent_2. The rest are from parent_1
        child_2 = (parent_2 & front_mask) | (parent_1 & back_mask)

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
    current_score = 0
    for i in range(bits):
        # Cycle through all bits. Increment score if current bit is
        # equal in both the chromosome and the target
        if ((chrom >> i) & 1) == ((target >> i) & 1):
            current_score += 1

    return current_score


def plot_averages(averages, total_iter):
    plt.plot(range(1, total_iter+1), averages, marker='o')
    plt.title(f'Average fitness over {total_iter} '
              'generations (Target String)')
    plt.xlabel('Generation')
    plt.ylabel('Average fitness')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
