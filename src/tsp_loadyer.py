import gzip

def load_tsp(filepath):
    cities = []
    reading = False
    with gzip.open(filepath, 'rt') as f:
        for line in f:
            if line.strip() == "NODE_COORD_SECTION":
                reading = True
                continue
            if line.strip() == "EOF":
                break
            if reading:
                _, x, y = line.split()
                cities.append((float(x), float(y)))
    return cities

berlin = load_tsp('data/berlin52.tsp.gz')
kroA100 = load_tsp('data/kroA100.tsp.gz')