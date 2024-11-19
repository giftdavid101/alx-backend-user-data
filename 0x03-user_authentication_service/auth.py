#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from db import DB, User


def _generate_uuid() -> str:
    """Generates a random uuid string
    """
    from uuid import uuid4
    return str(uuid4())

def _hash_password(password: str) -> bytes:
    """Encrypts a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Creates a new user if the email does not exist
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User %s already exists" % email)

