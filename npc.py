import xlrd
import json
import pygame
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
        self.position = [int(cellsArray[2]), int(cellsArray[3])]
        self.sprite = pygame.image.load("./textures/characters/" + cellsArray[4])
        self.dialogues = []

        # Collision coordinates
        self.npc_left_dialogue = self.position[0] - 0.5*TILESIZE
        self.npc_right_dialogue = self.position[0] + 0.5*TILESIZE
        self.npc_top_dialogue = self.position[1] - 0.5*TILESIZE
        self.npc_bottom_dialogue = self.position[1] + 0.5*TILESIZE

    def isCollision(self, player_X, player_Y):
        print("Just checkin' collision with NPC")
        if player_X >= self.npc_left_dialogue and player_X <= self.npc_right_dialogue and player_Y >= self.npc_top_dialogue and player_Y <= self.npc_bottom_dialogue:
            return True
        return False

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