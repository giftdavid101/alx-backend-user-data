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

@app.errorhandler(403)
def unauthorized(error) -> str:
    """ Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.route("/")
def home() -> str:
    """
    Home route
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    Register a new user route
    """
    email, password = request.form.get('email'), request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": "%s" % email, "message": "user created"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
