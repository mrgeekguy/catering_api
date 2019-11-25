from flask import Blueprint, request
# Blueprint sets up blueprints
# Request sets up HTML calls

user_auth = Blueprint("auth_api", __name__)

# user login route
@user_auth.route("/login", methods=["POST"])
def login():
    # user login
    # TODO auth token via JWT Token
    # Body: {email, password}
    # Return: {auth_token}
    body = request.json
    pass

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


