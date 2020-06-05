import pygame
from settings import *

class Castle:
    def __init__(self):
        self.SPRITE = pygame.image.load('./textures/buildings/castle/castle.png')
        self.POS = [1024,896]
        #self.POS = [0,0]
        self.MOVING = False
        self.castle_entrance_left = self.POS[0] + 150 - TILESIZE
        self.castle_entrance_right = self.POS[0] + 150 + 0.5*TILESIZE
        self.castle_entrance_top = self.POS[1] + 300 - TILESIZE
        self.castle_entrance_bottom = self.POS[1] + 300 - 0.25*TILESIZE

    def checkCastleEntrance(self, player_X, player_Y):
        if player_X >= self.castle_entrance_left and player_X <= self.castle_entrance_right and player_Y <= self.castle_entrance_bottom and player_Y >= self.castle_entrance_top:
            return True
        return False