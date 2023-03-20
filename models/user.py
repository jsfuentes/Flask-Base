from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer

from .database import db


class Base(DeclarativeBase):
    pass


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
