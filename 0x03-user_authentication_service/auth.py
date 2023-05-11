#!/usr/bin/env python3
"""Auth"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """salting password and hashing"""
    salt_pass = password.encode('utf-8')
    new_password = bcrypt.hashpw(salt_pass, bcrypt.gensalt())
    return new_password
