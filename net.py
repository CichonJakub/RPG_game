import socketio
from typing import List
import json
from worrior import Worrior

sio = socketio.Client()

allPlayers = []
otherPlayers = []

class ServerPlayer:
    def __init__(self, name, map, posX, posY, sprite):
        self.name = name
        self.map = map
        self.posX = posX
        self.posY = posY
        self.sprite = sprite

    @classmethod
    def from_json(cls, data):
        return cls(**data)

class PlayersToSend:
    def __init__(self, players: List[Worrior]):
        self.players = players

    @classmethod
    def from_json(cls, data):
        players = list(map(Worrior.from_json, data["players"]))
        return cls(players)

class Net:
    @sio.event
    def connect():
        print('connection established')

    @sio.on('helloBack')
    def on_message(data):
        print(data)

    @sio.event
    def disconnect():
        print('disconnected from server')

    @sio.on('allPlayersTable')
    def on_message(data):
        global allPlayers
        print("ALL PLAYERS:")
        print(data)
        print(len(json.loads(data)))
        allPlayers = json.loads(data)

    @sio.on('newPlayerAnnounced')
    def on_message(data):
        #print("New Player:")
        #print(data)
        data_dict = json.loads(data)
        otherPlayers.append(data_dict)

    @sio.on('existingPlayers')
    def on_message(data):
        global otherPlayers
        #print("Existing Players:")
        #print(data)
        data_dict = json.loads(data)#PlayersToSend.from_json(json.loads(data))
        print(data_dict)
        otherPlayers = data_dict['players']
        print("EXISTING ADDED")

    @sio.on('updateOtherPlayers')
    def on_message(data):
        #print("DATA:")
        #print(data)
        data_dict = json.loads(data)
        modified = next((x for x in otherPlayers if x['name'] == data_dict['name']), None)
        if modified != None:
            modified['position_x'] = data_dict['position_x']
            modified['position_y'] = data_dict['position_y']
            modified['map'] = data_dict['map']
            #print("PLAYER MOVEMENT UPDATED " + str(modified['posX']) + " " + str(modified['posY']))

    def connectToServer(self):
        sio.connect('http://localhost:5000')
        sio.emit('hello', 'message from the CLIENT')
        #sio.wait()

    def putPlayer(self, worriorObject):
        sendString = json.dumps(worriorObject.__dict__)
        #print(sendString)
        sio.emit('newPlayer', sendString)

    def sendMove(self, worriorObject):
        sendString = json.dumps(worriorObject.__dict__)
        #print(sendString)
        sio.emit('sendMove', sendString)

    @property
    def getOtherPlayers(self):
        return otherPlayers

    @property
    def getAllPlayers(self):
        return allPlayers

def is_in_DB(nick):
    playerData = next((x for x in allPlayers if x['name'] == nick), None)
    if playerData == None:
        return False
    else:
        return True

def askForPlayerData(nick):
    playerData = next((x for x in allPlayers if x['name'] == nick), None)
    if playerData == None:
        return None
    else:
        return playerData
