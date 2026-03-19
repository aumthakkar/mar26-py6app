from flask import Flask, jsonify
import time
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
       "time" : time.ctime(),
       "host" : socket.gethostname(),
       "env" : "dev",
       "msg" : "Hi Pranav! How are you?"
    })


@app.route('/api/v1/healthz')
def hello_world():
    return jsonify({
        "status" : "up"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")