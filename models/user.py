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


def get_user(id):
    user = db.get_or_404(User, id)
    return user


def insert_user():
    user = User(
        username="girl",
        email="jsjfuenetesj@gmail.com",
    )
    db.session.add(user)
    db.session.commit()
    return user
