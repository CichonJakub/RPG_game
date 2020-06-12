import socketio

sio = socketio.Client()


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
