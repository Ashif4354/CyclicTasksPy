from src import main
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'message': 'Cyclic Tasks is running...'})

        