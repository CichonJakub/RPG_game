import xlrd
import json
import pygame
from settings import *
from dialogues import *

loc = ("./data/locations.xlsx")
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#print(sheet.cell_value(0, 0))
#print(sheet.row_values(1))
print(sheet.nrows)

class LOCATIONS:
    def __init__(self, cellsArray):
        self.location_id = cellsArray[0]
        self.map = "maps/" + cellsArray[1] + ".txt"
        self.next_map = "maps/" + cellsArray[9] + ".txt"
        self.position = [int(cellsArray[2]), int(cellsArray[3])]
        self.sprite = pygame.image.load("./textures/buildings/castle/" + cellsArray[8])

        # Collision coordinates
        self.interact_left = cellsArray[4]
        self.interact_right = cellsArray[5]
        self.interact_top = cellsArray[6]
        self.interact_bottom = cellsArray[7]

    def checkInteraction(self, player_X, player_Y):
        if player_X >= self.interact_left and player_X <= self.interact_right and player_Y <= self.interact_bottom and player_Y >= self.interact_top:
            return True
        return False

def importLocations(self):
    locArray = []
    for i in range(1, sheet.nrows):
        tmp = sheet.row_values(i)
        tmpLoc = LOCATIONS(tmp)
        locArray.append(tmpLoc)
    
    return locArray