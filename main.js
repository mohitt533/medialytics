'use strict';
const {app, BrowserWindow} = require('electron')
const url = require('url')
const path = require('path')
try {
	require('electron-reload')(__dirname);
} catch (err) {}
let win

function createWindow() {
   win = new BrowserWindow({width: 1500, height: 1000})
   win.loadURL(url.format ({
      pathname: path.join(__dirname, 'index.html'),
      protocol: 'file:',
      slashes: true
   }))
}

app.on('ready', createWindow)
