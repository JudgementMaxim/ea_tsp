from tsp_loader import load_tsp

berlin_tsp = load_tsp('data/berlin52.tsp.gz')

mutation_prob = 0.1  # 10% Wahrscheinlichkeit
mu = 20              # Eltern
lam = 100            # Kinder