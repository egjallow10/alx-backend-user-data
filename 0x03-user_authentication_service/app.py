#!/usr/bin/env python3
"""Basic flash app"""


from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def home_page():
    """simple basic flash app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
