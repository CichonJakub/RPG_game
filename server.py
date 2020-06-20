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
    print("DATA RECEIVING")
    print(data)
    data_dict = json.loads(data)
    print(data_dict)
    player = Player(sid, data_dict['name'], data_dict['map'], data_dict['posX'], data_dict['posY'], data_dict['sprite'])
    print(sid + " " + data_dict['name'] + " " + data_dict['map'])
    players.append(player)
    sio.emit('existingPlayers', json.dumps(players.__dict__), room=sid)
    sio.emit('newPlayerAnnounced', data, skip_sid=sid)

@sio.on('sendMove')
def on_message(sid, data):
    print("PLAYER MOVING")
    data_dict = json.loads(data)
    modified = next((x for x in players if x.name == data_dict['name']), None)
    if modified != None:
        modified.position[0] = data_dict['posX']
        modified.position[1] = data_dict['posY']
        print("PLAYER MOVEMENT UPDATED " + str(modified.position[0]) + " " + str(modified.position[1]))
        sio.emit('updateOtherPlayers', data, skip_sid=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
