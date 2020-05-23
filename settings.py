import pygame

# game settings
FPS = 60
TITLE = "POKEMON"

# grid settings
TILESIZE = 64
MAPWIDTH = 20
MAPHEIGHT = 10
WIDTH = MAPWIDTH * TILESIZE
HEIGHT = MAPHEIGHT * TILESIZE
MAP = 'maps/second_map.txt'

# TILES
# przekształcić na dict
#DIRT = 0
#GRASS = 1
#WATER = 2

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    'DIRT': pygame.image.load('textures/dirt.png'),
    'GRASS': pygame.image.load('textures/grass.png'),
    'WATER': pygame.image.load('textures/water.png')
}