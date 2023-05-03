#!/usr/bin/env python3
"""
Class templete for all authorization
"""

from flask import request
from typing import List, TypeVar


from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to require authentication for a given path.

        Args:
            path (str): The path to require authentication for.
            excluded_paths (List[str]): A list of paths to exclude
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to get the authorization header from a Flask request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            str: The value of the authorization header, or None if the
            header is not present.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user from a Flask request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current user, or
            None if no user is authenticated.
        """
        return None
