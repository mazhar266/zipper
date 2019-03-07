from flask import Flask, jsonify

from config import SETTINGS

app = Flask(__name__)

# the root url containing app info
@app.route('/')
def info():
    return jsonify(SETTINGS["INFO"])
