import pygame
import sys
pygame.init()
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
WIDTH_BATTLE = 5 * TILESIZE
HEIGHT_BATTLE = 5 * TILESIZE
MAP_BATTLE = 'maps/battlefield.txt'

LOCKED_TILES = ['WATER', 'STONE']
ENTRANCE = ['DOOR']

background = (43, 45, 56)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
#font = pygame.font.SysFont(None, 20)
font2 = pygame.font.Font('freesansbold.ttf', 24)


plus2 = pygame.image.load('textures\signs\plus2.png')
plus2 = pygame.transform.scale(plus2, (76, 76))


minus2 = pygame.image.load('textures\signs\minus2.png')
minus2 = pygame.transform.scale(minus2, (76, 76))


# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    'DIRT': pygame.image.load('textures/dirt.png'),
    'GRASS': pygame.image.load('textures/grass.png'),
    'WALL': pygame.image.load('textures/wall.png'),
    'WATER': pygame.image.load('textures/water.png'),
    'STONE': pygame.image.load('textures/stone.jpg'),
    'DOOR': pygame.image.load('textures/locations/door.png'),
}

white = (255, 255, 255) 
black = (0, 0, 0) 
blue = (0, 0, 128) 

subtitles_speed = 0.03