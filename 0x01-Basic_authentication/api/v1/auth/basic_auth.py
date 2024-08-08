#!/usr/bin/env python3
"""implementation of basic_auth that inherits from auth"""

import base64
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
