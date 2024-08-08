#!/usr/bin/env python3
"""class implementation of Auth"""


from flask import request
from typing import List, TypeVar


class Auth:
    """class implementation of Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> str:
        """
        returns false path and excluded paths
        """
        return (path, excluded_paths)

    def authorization_header(self, request=None) -> str:
        """returns None"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
