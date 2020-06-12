//server.js
const http = require('http');
const fs = require('fs');
const socket = require('socket.io');
const express = require('express');
const app = require('express')();
const server = require('http').Server(app);
const io = require('socket.io')(server);

const port = 5000;

app.listen(port, () => console.log(`App listening on port ${port}!`));

connectedPlayers = [];

io.on('connection', function (socket) {

    console.log("Connecting");
    connectedPlayers.push({socket: socket});

    socket.on('hello', function(data){
        console.log(data);
    })

    socket.on('disconnect', function(data){
        let index = connectedPlayers.findIndex(obj => obj.socket == socket);
        if( index != -1 ){
            connectedPlayers.splice(i,1);
        }
    })

});
