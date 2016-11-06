from flask import Flask, jsonify


class Server(object):
    
    app = None

    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = '7q%3=;8J+X5:f.+pU9e!;6x:E*n_9^Ky0~.R'

        @self.app.route('/')
        def home():
            return jsonify({
                "ping": "pong"
            })
