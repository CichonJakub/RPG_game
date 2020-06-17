import socketio
import json

sio = socketio.Client()

class PlayerToSend:
    def __init__(self, name, map, posX, posY, sprite):
        self.name = name
        self.map = map
        self.posX = posX
        self.posY = posY
        self.sprite = sprite

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

    def connectToServer(self):
        sio.connect('http://localhost:5000')
        sio.emit('hello', 'message from the CLIENT')
        #sio.wait()

    def putPlayer(self, name, map, posX, posY, sprite):
        sendString = json.dumps(PlayerToSend(name, map, posX, posY, sprite).__dict__)
        print(sendString)
        sio.emit('newPlayer', sendString)
