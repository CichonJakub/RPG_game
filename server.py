import eventlet
import socketio
from typing import List
import json

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

players = []

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

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
    player = ServerPlayer(data_dict['name'], data_dict['map'], data_dict['posX'], data_dict['posY'], data_dict['sprite'])
    #print(sid + " " + data_dict['name'] + " " + data_dict['map'])
    players.append(player)
    #print("PLAYERS: ")
    #print(players)
    sio.emit('newPlayerAnnounced', data, skip_sid=sid)
    #print("EMIT1")
    if len(players) > 1:
        arrayToSend = PlayersToSend(players)
        jsonString = json.dumps(arrayToSend, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        sio.emit('existingPlayers', jsonString, room=sid)
        #print("EMIT2")

@sio.on('sendMove')
def on_message(sid, data):
    #print("PLAYER MOVING")
    data_dict = json.loads(data)
    modified = next((x for x in players if x.name == data_dict['name']), None)
    if modified != None:
        modified.posX = data_dict['posX']
        modified.posY = data_dict['posY']
        #print("PLAYER MOVEMENT UPDATED " + str(modified.position[0]) + " " + str(modified.position[1]))
        sio.emit('updateOtherPlayers', data, skip_sid=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
