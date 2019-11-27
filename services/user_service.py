from models.client import Client

def create_client(email, password, name, surname):
    new_client = Client(email, password, name, surname=None)
    return new_client.save()

def delete_client(id):
    