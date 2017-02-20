from random import choice, random
from string import ascii_letters as letters

from colorama import Fore, Style

ALPHABET = letters + ' '
MUTATION_RATE = 0.05
POPULATION_SIZE = 100


def fitness_function(target, population):
    distance = 0
    possibilities = {}
    for element in population:
        for k, j in zip(target, element):
            if k != j:
                distance += 1
        possibilities[''.join(element)] = distance
        distance = 0
    return possibilities


def mutate(population):
    return [(choice(ALPHABET) if random() < MUTATION_RATE else _) for _ in population]


def main(target, population):
    iterations = 0
    while target != list(population):
        population = [mutate(population) for _ in range(POPULATION_SIZE)]
        fitness = fitness_function(target=target, population=population)
        best_distance = min(fitness.values())
        best_fitness = min(fitness, key=fitness.get)
        population = best_fitness
        colorized_text = colorize(best_fitness=best_fitness, target=target)
        iterations += 1
        print("Iterations: {} - {} - Distance: {}".format(iterations, colorized_text, best_distance))


def colorize(best_fitness, target):
    colorized_text = ''
    for i, j in zip(best_fitness, target):
        if i != j:
            colorized_text += Fore.RED + i
        else:
            colorized_text += Fore.GREEN + i
    return colorized_text + Style.RESET_ALL


if __name__ == '__main__':
    target = list(input("Enter target word: "))
    population = [choice(ALPHABET) for i in range(len(target))]
    main(target=target, population=population)
