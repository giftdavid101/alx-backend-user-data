#!/usr/bin/env python3
"""
A User authentication service application
"""
from flask import Flask
from flask import (
    abort, jsonify,
    request, make_response, redirect
)

from auth import Auth

AUTH = Auth()

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
