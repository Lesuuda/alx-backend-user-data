#!/usr/bin/env python3
"""implementation of basic_auth that inherits from auth"""


from api.v1.auth.auth import Auth


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
