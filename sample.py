from flask import Flask

app = Flask(__name__)
app.debug = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ta')
def hello_ta():
    return 'Hello, TA!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)