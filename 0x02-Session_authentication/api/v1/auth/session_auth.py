#!/usr/bin/env python3
"""class for session auth"""


from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class impmenetation for session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session id for user id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user id based on session id"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
