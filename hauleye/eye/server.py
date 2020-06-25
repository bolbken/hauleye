from flask import Flask


app = Flask(__name__)

@app.route('/stream')
def hello_world():
    return 'worked'

@app.route('/secure')
def hello_world():
    return 'worked'