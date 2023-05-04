#!/usr/bin/env python3
"""
Class templete for all authorization
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to require authentication"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header fr"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user """
        return None
