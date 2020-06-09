import xlrd
import json

# Give the location of the file
loc = ("./data/quest_dialogues_data.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)

#print(sheet.cell_value(0, 0))
#print(sheet.row_values(1))
print(sheet.nrows)

class DLine:
    def __init__(self, cellsArray):
        self.npc = cellsArray[0]
        self.questId = cellsArray[1]
        self.stage = cellsArray[2]
        self.player = cellsArray[3]
        self.segment = cellsArray[4]
        self.option = cellsArray[5]
        self.reqs = cellsArray[6]
        self.text = cellsArray[7]
        self.reward = cellsArray[8]
        self.next = []

def importDialogueTree(self):
    dialoguesArray = []

    for i in range(1, sheet.nrows):
        lineAdded = False
        tmp = sheet.row_values(i)
        tmpLine = DLine(tmp)
        #print(tmpLine.text)
        if( tmpLine.segment == 1 or tmpLine.segment == 0 ):
            dialoguesArray.append(tmpLine)
            lineAdded = True
        else:
            for y in range(len(dialoguesArray)):
                if dialoguesArray[y].questId == tmpLine.questId and dialoguesArray[y].stage == tmpLine.stage:
                    tmpAppending = dialoguesArray[y]
                    while lineAdded != True:
                        if len(tmpAppending.next) == 0 and tmpAppending.segment == tmpLine.segment-1:
                            tmpAppending.next.append(tmpLine)
                            lineAdded = True
                        elif len(tmpAppending.next) >= 1:
                            if( tmpAppending.next[0].segment == tmpLine.segment and tmpAppending.next[0].option != tmpLine.option ):
                                tmpAppending.next.append(tmpLine)
                                lineAdded = True
                            elif len(tmpAppending.next) == 1 and tmpAppending.next[0].segment < tmpLine.segment:
                                tmpAppending = tmpAppending.next[0]
                            else:
                                for z in range(len(tmpAppending.next)):
                                    if tmpAppending.next[z].option == tmpLine.option and tmpAppending.next[z].segment < tmpLine.segment:
                                        tmpAppending = tmpAppending.next[z]
                                        break
                if lineAdded == True:
                    break

    #print( len(dialoguesArray) )
    #print( dialoguesArray[0].next[0].next[2].next[0].text )
    return dialoguesArray