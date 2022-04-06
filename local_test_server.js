/*
var http = require('http');
var express = require('express');
var app = express();
app.get('/test', function (request, response) {
    //response.sendFile(__dirname + '/data.json');
});
var server = http.createServer(app);
var io = require('socket.io')(server);
const bodyParser = require('body-parser'); 
const path = require('path');
const {execFile, exec, spawn} = require ('child_process');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));   
app.use(express.json());

app.post('/test', function(req, res){                 
    //res.sendFile(__dirname + '/public/status.html');
    var info = req.body;
    io.emit('messageFromServer', info);
    console.log(info)
    res.send(info);
});

server.listen(8000, console.log("listening to port 8000"));
*/

const express = require('express');

const app = express();
const port = process.env.PORT || 8000;

// routes will go here


app.get('/test', function(req, res) {
    res.send(req.query);
    console.log(req.query);
  });


app.listen(port);
console.log('Server started at http://localhost:' + port);
