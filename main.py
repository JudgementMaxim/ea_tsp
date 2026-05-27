import random

from src.ea import ea
from src.representation import random_tour, tour_length
from src.operators import crossover, mutate
from src.selection import selection
from src.tsp_loader import load_tsp

berlin = load_tsp('data/berlin52.tsp.gz')

mu = 20
lam = 100
mutation_prob = 0.1
generations = 500

best_tour = ea(berlin, mu, lam, mutation_prob, generations)
print(f"Beste Tourlänge: {tour_length(best_tour, berlin)}")