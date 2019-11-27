from . import bcrypt
from flask_jwt_extended import create_access_token

def generate_password_hash(password):
    my_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    return my_hash

def check_password_hash(password):
    my_hash_check = bcrypt.check_password_hash(password)
    return my_hash_check

