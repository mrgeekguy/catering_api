from models.client import Client
from auth_service import generate_password_hash, check_password_hash, create_access_token
from services import bcrypt

def create_client(email, password, name, surname):
    if not Client.get_client(email):
        password = generate_password_hash(password)
        new_client = Client(email, password, name, surname)
        new_client.save()
    else:
        return "Client already registered"

def delete_client(id):
    