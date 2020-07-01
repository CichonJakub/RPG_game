import eventlet
import socketio
from typing import List
import json
from worrior import Worrior

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

players = []
activePlayers = []

def loadPlayersBase():
    with open("playersBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        print(len(jsonObject['players']))
        #print(jsonObject[0]['name'])
        players = jsonObject['players']
        print(players)
        jsonFile.close()
        return players

def savePlayersBase():
        print("SAVING PLAYERS TO FILE")
        file = open("playersBase.json","w")
        arrayToSave = PlayersToSend(players)
        jsonString = json.dumps(arrayToSave, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        file.write(jsonString)
        file.close()
        print("SAVING DONE")

loadPlayersBase()

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    players = loadPlayersBase()
    print('connect ', sid)
    print(players)
    jsonString = json.dumps(players)
    #print(jsonString)
    sio.emit('allPlayersTable', jsonString, room=sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.on('hello')
def on_message(sid, data):
    print(data)
    sio.emit('helloBack', 'Message from the server')

@sio.on('newPlayer')
def on_message(sid, data):
    #print("DATA RECEIVING")
    #print(data)
    data_dict = json.loads(data)
    #print(data_dict)
    player = data_dict
    #print(sid + " " + data_dict['name'] + " " + data_dict['map'])
    existingPlayer = next((x for x in players if x['name'] == data_dict['name']), None)
    if existingPlayer == None:
        print("APPENDING PLAYER")
        players.append(player)
    activePlayers.append(player)
    #print("PLAYERS: ")
    #print(players)
    sio.emit('newPlayerAnnounced', data, skip_sid=sid)
    #print("EMIT1")
    if len(players) > 1:
        arrayToSend = PlayersToSend(activePlayers)
        jsonString = json.dumps(arrayToSend, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        sio.emit('existingPlayers', jsonString, room=sid)
        #print("EMIT2")

@sio.on('sendMove')
def on_message(sid, data):
    print("PLAYER MOVING")
    print(data)
    data_dict = json.loads(data)
    print(data_dict)
    modifiedPlayer = next((x for x in players if x['name'] == data_dict['name']), None)
    if modifiedPlayer != None:
        modifiedPlayer = data_dict
    modified = next((x for x in activePlayers if x['name'] == data_dict['name']), None)
    if modified != None:
        modified['position_x'] = data_dict['position_x']
        modified['position_y'] = data_dict['position_y']
        modified['map'] = data_dict['map']
        #print("PLAYER MOVEMENT UPDATED " + str(modified.position[0]) + " " + str(modified.position[1]))
        sio.emit('updateOtherPlayers', data, skip_sid=sid)
        savePlayersBase()

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
