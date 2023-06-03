import math

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(distance)

def nearest_neighbour(cities):
    current_city = cities[0]
    
    path = [current_city]
    remaining_cities = set(cities[1:])
    
    while remaining_cities:
        nearest_city = min(remaining_cities, key=lambda x : distance(x, current_city))
        
        path.append(nearest_city)
        remaining_cities.remove(nearest_city)
        current_city = nearest_city
        
    return path



