import random


def crossover(parent1, parent2):
    i,j = sorted(random.sample(range(len(parent1)), 2))

    child = [None]*len(parent1)
    child[i:j] = parent1[i:j]

    pos = 0
    for city in parent2:
        if city not in child:
            while child[pos] is not None:
                pos += 1
            child[pos] = city

    return child

def mutate(tour, mutation_prob):
    if random.random() < mutation_prob:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour