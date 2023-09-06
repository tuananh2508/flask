from flask import Flask
import os

app = Flask(__name__)
app.debug = bool(os.getenv('FLASK_DEBUG', False))
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
    app.run(host=os.getenv('FLASK_HOST', '127.0.0.1'), port=os.getenv('FLASK_PORT', 8080))