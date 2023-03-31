from flask import jsonify, request, current_app
from app.users import bp
from app.models.user import db_get_user, db_insert_user, db_get_user_by_email, db_get_create_google_user
from passlib.hash import pbkdf2_sha256
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_login import login_user, logout_user, current_user


@bp.route("/<int:id>")
def get_user(id):
    user = db_get_user(id)
    return jsonify(user and user.as_dict())


# TODO: Implement properly
@bp.route("/me", methods=["POST"])
def guess_user():
    print("CURRENT USER", current_user)
    if current_user.is_authenticated:
        print("CU", current_user and current_user.as_dict())
        return jsonify(current_user.as_dict())
    else:
        return ('', 204)
    # if not request.is_json:
    #     return jsonify({"msg": "Missing JSON in request"}), 400
    # id = request.json.get('id', None)
    # user = db_get_user(id)
    # return jsonify(user.as_dict())


@bp.route("/google_login", methods=["POST"])
def google_login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    token = request.json.get('token', None)
    print("Got Token", token)
    try:
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), current_app.config['GOOGLE_CLIENT_ID'])
        print("IDINFO", idinfo)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # ID token is valid
        email = idinfo['email']
        picture = idinfo['picture']
        name = idinfo['name']

        user = db_get_create_google_user(email, picture, name)
        login_user(user, remember=True)
        print("Logged in user", user.as_dict())
        return jsonify(user.as_dict())

    except ValueError:
        # Invalid token
        return jsonify({"msg": "Invalid token"}), 401


# TODO: Fix this
# @bp.route("/create", methods=["GET", "POST"])
# def insert_user():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     email = request.json.get('email', None)
#     password = request.json.get('password', None)

#     # generate new salt, and hash a password
#     # hash = pbkdf2_sha256.hash("toomanysecrets")
#     # # hash '$pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'

#     # pbkdf2_sha256.verify("toomanysecrets", hash)
#     # # True
#     # pbkdf2_sha256.verify("joshua", hash)
#     # # False

#     user = db_insert_user()
#     return jsonify(user.as_dict())


# @bp.route('/login', methods=['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     email = request.json.get('email', None)
#     password = request.json.get('password', None)

#     # generate new salt, and hash a password
#     # hash = pbkdf2_sha256.hash("toomanysecrets")
#     # # hash '$pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'

#     # pbkdf2_sha256.verify("toomanysecrets", hash)
#     # # True
#     # pbkdf2_sha256.verify("joshua", hash)
#     # # False

#     print("GOT", email, password)

#     if not email or not password:
#         return jsonify({"msg": "Missing username or password"}), 400

#     user = db_get_user_by_email(email)

#     if user is None or user.password != password:
#         return jsonify({"msg": "Invalid username or password"}), 401

#     access_token = create_access_token(identity=user.id)
#     return jsonify(access_token=access_token), 200


@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"msg": "Logged out"}), 200
