import eventlet
import socketio
import json

class Player:
    def __init__(self, sid, name, map, posX, posY, sprite):
        self.sid = sid
        self.name = name
        self.map = map
        self.position = [posX, posY]
        self.sprite = sprite

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
    print(data)
    data = json.loads(data)
    player = Player(sid, data.name, data.map, data.posX, data.posY, data.sprite)
    print(sid + " " + data.name + " " + data.map)
    players.append(player)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
