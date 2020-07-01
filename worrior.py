import random
import pygame
from settings import *


class Worrior():
    def __init__(self, name='xyz', sprite='./BULBA64.png',position_x=0, position_y=0, hp=100, ad=0, arm=0, pa=10):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.arm = arm
        self.pa = pa
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.prev_pos = []
        self.map = "maps/second_map.txt"
        self.prev_map = []
        self.gold = 100
        self.exp = 0
        self.dir = False
        self.moving = False
        self.velocity = 16
        self.curr_quests = {}
        self.quests_completed = []


    def __init__(self, ad=0, arm=0, curr_quests={}, dir=False, exp=0, gold = 0, hp=0, map='maps/second_map.txt', moving=False, name='noname', pa=10, position_x=0, position_y=0, prev_map=[], prev_pos=[], quests_completed=[], sprite='', velocity=16):
        self.ad = ad
        self.arm = arm
        self.curr_quests = curr_quests
        self.dir = dir
        self.exp = exp
        self.gold = gold
        self.hp = hp
        self.map = map
        self.moving = moving
        self.name = name
        self.pa = pa
        self.position_x = position_x
        self.position_y = position_y
        self.prev_map = prev_map
        self.prev_pos = prev_pos
        self.quests_completed = quests_completed
        self.sprite = sprite
        self.velocity = velocity


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

    @classmethod
    def from_json(cls, data):
        return cls(**data)
