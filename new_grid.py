import pygame
import random

# TILES
DIRT = 0
GRASS = 1
WATER = 2

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    DIRT: pygame.image.load('textures/dirt.png'),
    GRASS: pygame.image.load('textures/grass.png'),
    WATER: pygame.image.load('textures/water.png')
}

GRID = []
# TILES TO BE DISPLAYED
def render_map():
    global GRID
    map = 'maps/first_map.txt'
    with open(map, 'r') as f:
        for row in f:
            GRID.append(row.strip().split(','))

# GRID[kolumna][wiersz]
# print(GRID[-4][0])

# GAME DIMENSIONS, CONFIG
TILESIZE = 64
MAPWIDTH = 20
MAPHEIGHT = 10
pygame.init()
pygame.display.set_caption('PYGAME GAME')
# MAPHEIGHT + 125 for inventory
window = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
#window = pygame.display.set_mode((512,320))    // mniejsza mapa i potem próba przesuwania 