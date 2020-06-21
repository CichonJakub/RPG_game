import socketio
from typing import List
import json

sio = socketio.Client()

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
    def __init__(self, players: List[ServerPlayer]):
        self.players = players

    @classmethod
    def from_json(cls, data):
        players = list(map(ServerPlayer.from_json, data["players"]))
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

    @sio.on('newPlayerAnnounced')
    def on_message(data):
        #print("New Player:")
        #print(data)
        data_dict = json.loads(data)
        otherPlayers.append(data_dict)

    @sio.on('existingPlayers')
    def on_message(data):
        #print("Existing Players:")
        #print(data)
        data_dict = json.loads(data)#PlayersToSend.from_json(json.loads(data))
        print(data_dict)
        otherPlayers = data_dict['players']
        print("EXISTING ADDED")
        #print(otherPlayers)

    @sio.on('updateOtherPlayers')
    def on_message(data):
        #print("DATA:")
        #print(data)
        data_dict = json.loads(data)
        modified = next((x for x in otherPlayers if x['name'] == data_dict['name']), None)
        if modified != None:
            modified['posX'] = data_dict['posX']
            modified['posY'] = data_dict['posY']
            #print("PLAYER MOVEMENT UPDATED " + str(modified['posX']) + " " + str(modified['posY']))

    def connectToServer(self):
        sio.connect('http://localhost:5000')
        sio.emit('hello', 'message from the CLIENT')
        #sio.wait()

    def putPlayer(self, name, map, posX, posY, sprite):
        sendString = json.dumps(ServerPlayer(name, map, posX, posY, sprite).__dict__)
        #print(sendString)
        sio.emit('newPlayer', sendString)

    def sendMove(self, name, map, posX, posY, sprite):
        sendString = json.dumps(ServerPlayer(name, map, posX, posY, sprite).__dict__)
        #print(sendString)
        sio.emit('sendMove', sendString)
