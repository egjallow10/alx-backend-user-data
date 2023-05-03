#!/usr/bin/env python3
"""
Class templete for all authorization
"""

from flask import request
from typing import List, TypeVar
from flask import request


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to require authentication for a given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to get the authorization header from a Flask request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user from a Flask request.
        """
        return None
