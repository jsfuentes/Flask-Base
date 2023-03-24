from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def db_get_user(id):
    user = db.get_or_404(User, id)
    return user


def db_insert_user():
    user = User(
        username="girl",
        email="jsjfuenetesj@gmail.com",
    )
    db.session.add(user)
    db.session.commit()
    return user
