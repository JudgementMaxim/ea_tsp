from tsp_loader import load_tsp
from representation import tour_length
from ea import ea

berlin = load_tsp('data/berlin52.tsp.gz')

mu = 20
lam = 100
mutation_prob = 0.1
generations = 500

best_tour = ea(berlin, mu, lam, mutation_prob, generations)
print(f"Beste Tourlänge: {tour_length(best_tour, berlin)}")