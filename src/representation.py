import random
import math

def random_tour(n):
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def tour_length(tour, cities):
    tour_length = 0
    for i in range(len(tour)):
        city_a = cities[tour[i]]
        city_b = cities[tour[(i+1)%len(tour)]]
        dx = city_b[0] - city_a[0]
        dy = city_b[1] - city_a[1]
        tour_length += math.sqrt(dx**2 + dy**2)
    return tour_length


