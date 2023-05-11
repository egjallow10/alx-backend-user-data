#!/usr/bin/env python3
"""Auth"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """salting password and hashing"""
    salt_pass = password.encode('utf-8')
    new_password = bcrypt.hashpw(salt_pass, bcrypt.gensalt())
    return new_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ returns a new users

        Args:
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            User: _description_
        """

        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exits".format(user.email))
        except NoResultFound:
            pass
        hassed_password = _hash_password(password)
        new_user = self._db.add_user(email, hassed_password)
        return new_user
