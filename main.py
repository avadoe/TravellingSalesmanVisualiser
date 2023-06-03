# Nearest Neighbor Heuristic Implementation

import pygame
import travel
import math

WIDTH = 800
MARGIN = 25
BACKGROUNDCOLOR = (255, 255, 255)
CITYCOLOR = (0, 0, 128)
PATHCOLOR = (100, 100, 100)
CITYRADIUS = 10
PATHWIDTH = 3

CITIES = [
    (0, 0),
    (1, 5),
    (3, 2),
    (4, 7),
    (6, 3),
    (7, 8),
    (9, 6),
    (10, 1)
]

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Travelling Salesman')

def max_coor_dis(cities):
    max_dis = 0
    max_x, max_y = 0, 0
    for city in cities:
        if travel.distance((0, 0), city) > max_dis:
            max_dis = travel.distance((0, 0), city)
            max_x, max_y = city[0], city[1]
            
    return max(max_x, max_y)

# so (width, width) can be (max_x, max_y)

factor = max_coor_dis(cities=CITIES)

scaled_cities = []
for city in CITIES:
    scaled_x = city[0] * math.floor((WIDTH - 2 * MARGIN) / (factor + 1))
    scaled_y = city[1] * math.floor((WIDTH - 2 * MARGIN) / (factor + 1))
    scaled_cities.append((scaled_x, scaled_y))
    
for city in scaled_cities:
    if city == (0, 0):
        scaled_cities.remove(city)
        scaled_cities.append((MARGIN, MARGIN))

def draw(cities, path):
    WINDOW.fill(BACKGROUNDCOLOR)
    
    for city in scaled_cities:
        pygame.draw.circle(WINDOW, CITYCOLOR, city, CITYRADIUS)
        if city[0] == MARGIN and city[1] == MARGIN:
            x_val, y_val = 0, 0
        else: 
            x_val = city[0] * (factor + 1) / (WIDTH - 2 * MARGIN)
            y_val = city[1] * (factor + 1) / (WIDTH - 2 * MARGIN)
        text = f"({x_val}, {y_val})" 
        font = pygame.font.Font(None, 20)
        text_surface = font.render(text, True, CITYCOLOR)  
        text_rect = text_surface.get_rect()  
        text_rect.center = (city[0] + CITYRADIUS + 20, city[1])  
        WINDOW.blit(text_surface, text_rect) 
        
    for i in range(len(path) - 1):
        pygame.draw.line(WINDOW, PATHCOLOR, path[i], path[i + 1], PATHWIDTH)
        pygame.display.update()
        pygame.time.delay(1000)
        
    pygame.display.update()
    pygame.time.delay(1000)
    
shortest_path = travel.nearest_neighbour(cities=scaled_cities)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            
    draw(cities=CITIES, path=shortest_path)
    
pygame.quit()