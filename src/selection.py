from src.representation import tour_length

def selection(population, cities, mu):
    sorted_pop = sorted(population, key=lambda tour: tour_length(tour, cities))
    return sorted_pop[:mu]