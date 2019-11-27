from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from services import bcrypt


user_auth = Blueprint("auth_api", __name__)

# user login route
@user_auth.route("/login", methods=["POST"])
def login():
    body = request.json
    

@user_auth.route("/logout", methods=["POST"])
def logout():
    # deauthenticate token
    return "User logged out."

@user_auth.route("/register", methods=["POST"])
def register():
    # create user
    # body {email, password, name, surname}
    # return { "User successfully created" }
    pass


