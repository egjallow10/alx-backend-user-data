#!/usr/bin/env python3
""" templete for all authorization
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to require authentication
        """

        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user """
        return None
