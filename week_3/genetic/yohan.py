'''
1. Initialize Population
- Loop
    2. Evaluation
    3. Selection
    4. Crossover
    5. Mutation
6. Done

https://arxiv.org/pdf/1802.02006.pdf
'''

import random
import numpy as np


def init_population(n):
    population = []
    chromosome = []
    for _ in range(100):
        if len(chromosome) == n:
            population.append(chromosome)
            chromosome = []
        chromosome.append(random.randint(1, n))
    return population


def calculate_fitness_value(chromosome):
    fitness_value = 0
    for row in range(len(chromosome)):
        column = chromosome[row]
        for i in range(row):
            if chromosome[i] == column or \
                    chromosome[i] + i == row + column or \
                    i - chromosome[i] == row - column:
                fitness_value += 1
    return fitness_value


def evaluate(population):
    fitness_values = []
    for i in range(len(population)):
        fitness_value = calculate_fitness_value(population[i])
        fitness_values.append(fitness_value)

    return fitness_values


def sort_by_ranks(population, fitness_values):
    sorted_population_by_ranks = [(chromosome, fitness_value) for chromosome, fitness_value in sorted(
        zip(population, fitness_values), key=lambda x: x[1])]
    return sorted_population_by_ranks


def select(sorted_population_by_ranks):
    return [population for population, _ in sorted_population_by_ranks][:10]
    # return [population for population, _ in sorted_population_by_ranks][:len(sorted_population_by_ranks) // 2]


def crossover(selected_population):
    length_of_selected_population = len(selected_population)
    divide_point_of_one_third = length_of_selected_population // 3
    divide_point_of_two_third = divide_point_of_one_third * 2

    crossovered_population = []
    for i in range(0, length_of_selected_population - 1, 2):
        crossovered_chromosome = []
        parent_1 = selected_population[i]
        parent_2 = selected_population[i + 1]

        crossovered_chromosome.extend(parent_2[:divide_point_of_one_third])
        crossovered_chromosome.extend(
            parent_1[divide_point_of_one_third:divide_point_of_two_third])
        crossovered_chromosome.extend(parent_2[divide_point_of_two_third:])

        crossovered_population.append(crossovered_chromosome)

        crossovered_chromosome = []
        crossovered_chromosome.extend(parent_1[:divide_point_of_one_third])
        crossovered_chromosome.extend(
            parent_2[divide_point_of_one_third:divide_point_of_two_third])
        crossovered_chromosome.extend(parent_1[divide_point_of_two_third:])
        crossovered_population.append(crossovered_chromosome)

    return crossovered_population


def mutate(crossovered_population):
    mutate_population = []

    for i in range(len(crossovered_population)):
        mutate_point_1 = random.randrange(len(crossovered_population[i]))
        mutate_point_2 = random.randrange(len(crossovered_population[i]))

        crossovered_population[i][mutate_point_1], crossovered_population[i][
            mutate_point_2] = crossovered_population[i][mutate_point_2], crossovered_population[i][mutate_point_1]

        mutate_population.append(crossovered_population[i])

    return mutate_population


def solve_n_queens_using_genetic_algorithm(n):
    population = init_population(n)

    generation = 0

    answer = []
    while len(answer) < 1:  # n == 5: 10, n == 10: 724

        fitness_values = evaluate(population)
        sorted_population_by_ranks = sort_by_ranks(population, fitness_values)

        selected_population = select(sorted_population_by_ranks)
        crossovered_population = crossover(selected_population)
        new_generated_population = mutate(
            selected_population + crossovered_population)

        fitness_values_of_new_generated_population = evaluate(
            new_generated_population)
        sorted_new_generated_population_by_ranks = sort_by_ranks(new_generated_population,
                                                                 fitness_values_of_new_generated_population)

        generation += 1

        if sorted_new_generated_population_by_ranks[0][0] not in answer and \
                sorted_new_generated_population_by_ranks[0][1] == 0:
            answer.append(sorted_new_generated_population_by_ranks[0][0])

        if generation % 10000 == 0:
            print(generation)

    return answer


if __name__ == "__main__":
    n = 10
    answer = solve_n_queens_using_genetic_algorithm(n)
    print(len(answer), answer)
