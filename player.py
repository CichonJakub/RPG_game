import pygame
import random
#import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('This will get logged')

# DRAFT, 99% never used in other classes

class Player:
    def __init__(self):
        self.NAME = str(random.randint(1,65001))
        self.SPRITE = pygame.image.load('./BULBA64.png')
        self.MAP = "maps/second_map.txt"
        self.POS = [0, 0]
        self.HEALTH = 100
        self.GOLD = 100
        self.EXP = 0
        self.DIR = False
        self.MOVING = False
        self.VELOCITY = 16
        self.PREV_POS = []
        self.CURR_QUESTS = {}
        self.QUESTS_COMPLETED = []
        