#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Create a user using session"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """find a record form Db"""
        try:
            find_user = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if find_user is None:
            raise NoResultFound
        return find_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """find a user and update it"""
        update_data = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(update_data, key):
                setattr(update_data, key, value)
            else:
                raise ValueError
