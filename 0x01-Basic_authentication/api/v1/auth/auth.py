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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None:
            return None
        
        request_header = request.get('Authorization')
        if not request_header:
            return None
        
            

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user """
        return None
