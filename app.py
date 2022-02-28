import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/github")
async def github():
    response = requests.get(
        "https://api.github.com/repos/Mohammadreza-v/flask_log/pulls"
    )
    return jsonify(response.json())


@app.get("/gitlab")
async def gitlab():
    return ""
