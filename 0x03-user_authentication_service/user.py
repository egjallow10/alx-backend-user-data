#!/usr/bin/env python3
"""USER SQLALCHEMY ORM """

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# engine = create_engine('sqlite:///:memory', echo=True)


class User(Base):
    """
    Args:
        Base (Class):
        description_: create a user table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
