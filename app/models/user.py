from app.extensions import db, login_manager
from flask_login import UserMixin
from sqlalchemy import select


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True)
    picture = db.Column(db.String, nullable=True)
    
    #time_created = db.Column(db.DateTime(
        #timezone=True), server_default=func.now())
    #time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@login_manager.user_loader
def load_user(user_id):
    return db_get_user(user_id)


def db_get_user(id):
    user = db.session.scalars(
        select(User).where(User.id == id)).first()
    # print("USER", user)
    return user


def db_get_user_by_email(email):
    user = db.session.scalars(select(User).where(User.email == email)).first()
    return user


def db_get_create_google_user(email, picture, name):
    user = db_get_user_by_email(email)

    if user is not None:
        print("Found user in db with email", email)
        return user

    newUser = db_insert_user(email, picture, name)
    return newUser


def db_insert_user(email, picture, name):
    newUser = User(
        email=email,
        picture=picture,
        name=name
    )
    db.session.add(newUser)
    # print("Created new user", newUser.as_dict())
    db.session.commit()
    return newUser
