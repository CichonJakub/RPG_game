import xlrd
import json
import pygame
import random
from settings import *
from dialogues import *

loc = ("./data/non_player_characters.xlsx")
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#print(sheet.cell_value(0, 0))
#print(sheet.row_values(1))
print(sheet.nrows)

class NPC:
    def __init__(self, cellsArray):
        self.npc_id = cellsArray[0]
        self.map = "maps/" + cellsArray[1] + ".txt"
        self.position_x = int(cellsArray[2])
        self.position_y = int(cellsArray[3])
        self.sprite = pygame.image.load("./textures/characters/" + cellsArray[4])
        self.dialogues = []
        self.name = cellsArray[5]
        self.hp = cellsArray[6]
        self.ad = cellsArray[7]
        self.arm = cellsArray[8]
        # Collision coordinates
        self.npc_left_dialogue = self.position_x - 0.5*TILESIZE
        self.npc_right_dialogue = self.position_x + 0.5*TILESIZE
        self.npc_top_dialogue = self.position_y - 0.5*TILESIZE
        self.npc_bottom_dialogue = self.position_y + 0.5*TILESIZE

    def isCollision(self, player_X, player_Y):
        print("Just checkin' collision with NPC")
        if player_X >= self.npc_left_dialogue and player_X <= self.npc_right_dialogue and player_Y >= self.npc_top_dialogue and player_Y <= self.npc_bottom_dialogue:
            return True
        return False

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

    def __str__(self):
        return self.name

def importNpc(self):
    npcArray = []
    dialoguesArray = importDialogueTree(self)
    for i in range(1, sheet.nrows):
        tmp = sheet.row_values(i)
        tmpNpc = NPC(tmp)
        npcArray.append(tmpNpc)

    for i in range(len(npcArray)):
        for y in range(len(dialoguesArray)):
            if dialoguesArray[y].npc == npcArray[i].npc_id:
                npcArray[i].dialogues.append(dialoguesArray[y])

    return npcArray