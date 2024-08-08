#!/usr/bin/env python3
"""implementation of basic_auth that inherits from auth"""

import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auht"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """perfoms base_64 ebcoding"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """implemnts basic base64 decode"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        split_pos = decoded_base64_authorization_header.find(':')
        if split_pos == -1:
            return None, None
        user_email = decoded_base64_authorization_header[:split_pos]
        user_password = decoded_base64_authorization_header[split_pos + 1:]
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        if not users or len(users) == 0:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request
        """
        authorization_header = self.authorization_header(request)
        if not authorization_header:
            return None

        base64_authorization = self.extract_base64_authorization_header
        (authorization_header)
        if not base64_authorization:
            return None

        decoded_base64 = self.decode_base64_authorization_header
        (base64_authorization)
        if not decoded_base64:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_base64)
        if not user_email or not user_pwd:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
