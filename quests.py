import xlrd
import json

# Give the location of the file
quest = ("./data/quest_dialogues_data.xlsx")

# To open Workbook
wb = xlrd.open_workbook(quest)
sheet = wb.sheet_by_index(0)
print(sheet.nrows)

class QUESTS:
    def __init__(self, cellsArray):
        self.questID = cellsArray[0]
        self.stage = cellsArray[1]
        self.endStage = cellsArray[2]
        self.desc = cellsArray[3]
        self.gold = cellsArray[4]
        self.item = cellsArray[5]
        self.exp = cellsArray[6]  

def importQuests(self):
    questArray = []
    for i in range(1, sheet.nrows):
        tmp = sheet.row_values(i)
        tmpLoc = QUESTS(tmp)
        questArray.append(tmpLoc)
    
    return questArray