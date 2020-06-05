import pygame

# game settings
FPS = 100
TITLE = "POKEMON"

# grid settings
TILESIZE = 64
MAPWIDTH = 20
MAPHEIGHT = 10
WIDTH = MAPWIDTH * TILESIZE
HEIGHT = MAPHEIGHT * TILESIZE
MAP = 'maps/second_map.txt'

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    'DIRT': pygame.image.load('textures/dirt.png'),
    'GRASS': pygame.image.load('textures/grass.png'),
    'WALL': pygame.image.load('textures/wall.png'),
    'WATER': pygame.image.load('textures/water.png'),
    'STONE': pygame.image.load('textures/stone.jpg'),
    'DOOR': pygame.image.load('textures/buildings/castle/door.png'),
}