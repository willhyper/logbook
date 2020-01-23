from flask import request, render_template
from flask_socketio import emit

from datetime import datetime
from . import data_holder
from .app import app, socket

def _broadcast(payload : dict):
    emit('emit', payload, broadcast=True, namespace='/')

def _emit(payload : dict):
    emit('emit', payload, broadcast=False, namespace='/')


@socket.on('connect')
def connect():
    for log in data_holder.view():
        _emit(log)

@socket.on('broadcast_event')
def log_via_websocket(message: dict):
    _log(message.get('data', None))
    
@app.route("/", methods=['POST'])
def log_via_http():
    message : dict = request.get_json()
    _log(message.get('data', None))
    return 'ack'

def _log(msg : str):
    _msg = str.strip(msg) if msg is not None else None
    if _msg:
        payload = {'timestamp' : str(datetime.now()), 'log': msg}
        data_holder.append(payload)
        _broadcast(payload)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')