//server.js
const http = require('http');
const fs = require('fs');
const socket = require('socket.io');
const express = require('express');
const app = express();

const port = 80;

app.listen(port, () => console.log(`App listening on port ${port}!`));
