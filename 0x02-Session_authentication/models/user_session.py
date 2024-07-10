#!/usr/bin/env python3
""" UserSession class definition
"""
from models.base import Base


class UserSession(Base):
    """UserSession class definition
    """

    def __init__(self, *args: list, **kwargs: dict):
        """UserSession class definition"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
