import xlrd
import json
import dialogues

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
        self.map = cellsArray[1]
        self.position = [cellsArray[2], cellsArray[3]]
        self.sprite = "./textures/characters/" + cellsArray[4]
        self.dialogues = []

def importNpc(self):
    npcArray = []
    dialoguesArray = importDialogueTree()
    for i in range(1, sheet.nrows):
        tmp = sheet.row_values(i)
        tmpNpc = NPC(tmp)
        npcArray.append(tmpNpc)

    for i in range(len(npcArray)):
        for y in range(len(dialoguesArray)):
            if dialoguesArray[y].npc == npcArray[i].npc_id:
                npcArray[i].dialogues.append(dialoguesArray[y])

    return npcArray
