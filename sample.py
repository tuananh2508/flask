from flask import Flask

app = Flask(__name__)
import os

app = Flask(__name__)
app.debug = os.getenv('FLASK_DEBUG', False)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet_ta')
def greet_ta():
    return 'Hello, TA!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)