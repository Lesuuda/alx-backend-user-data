#!/usr/bin/env python3
"""class implementation of Auth"""


from flask import request
from typing import List, TypeVar


class Auth:
    """class implementation of Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if path not in list of strings to exclude
        """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path is None:
            return True
        normalized_path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if excluded_path == normalized_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None"""
        if request is None:
            return None
        key = 'Authorizaion'
        if key not in request:
            return None
        return request.get(key)

    def current_user(self, request=None) -> TypeVar('User'):
        """currently returns None"""
        if request is None:
            return None
