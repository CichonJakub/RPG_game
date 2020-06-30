import random
import pygame
from settings import *


class Worrior():
    def __init__(self, name='xyz', sprite='./BULBA64.png',position_x=0, position_y=0, hp=100, ad=0, arm=0, pa=10):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.arm = arm
        self.sprite = pygame.image.load(sprite)
        self.position_x = position_x
        self.position_y = position_y
        self.pa = pa
        self.map = "maps/second_map.txt"
        self.gold = 100
        self.exp = 0
        self.dir = False
        self.moving = False
        self.velocity = 16
        self.prev_pos = []
        self.curr_quests = {}
        self.quests_completed = []


    def attack(self):
        return random.randint(0, self.ad)

    def defence(self):
        return random.randint(0, self.arm)

    def lost_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.name} has been slain")

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    # wypisywanie imion, przeładowanie funkcji, jak print(objekt) to wyswietli sie tylko imie
    def __str__(self):
        return self.name