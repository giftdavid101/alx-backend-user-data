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

