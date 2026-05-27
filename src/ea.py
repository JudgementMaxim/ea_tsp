import random
from representation import random_tour, tour_length
from operators import crossover, mutate
from selection import selection


def ea(cities, mu,lam, mutation_prob, generations):
    population =  [random_tour(len(cities)) for _ in range(mu)]

    for generation in range(generations):
        children = []
        for _ in range(lam):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_prob)
            children.append(child)

        population = selection(population + children, cities, mu)
    return population[0]