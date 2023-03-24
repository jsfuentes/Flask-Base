from flask import jsonify
from app.users import bp
from app.models.user import db_get_user, db_insert_user


@bp.route("/<int:id>")
def get_user(id):
    user = db_get_user(id)
    return jsonify(user.as_dict())


@bp.route("/create", methods=["GET", "POST"])
def insert_user():
    user = db_insert_user()
    return jsonify(user.as_dict())
