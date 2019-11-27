from . import db
from datetime import datetime
from marshmallow import Schema, fields

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, email, password, name, surname=None):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname

    def save(self):
        db.session.add(self)
        db.session.commit()
        return f"Client {self.name} added."

    @staticmethod
    def get_client(email):
        return Client.query.filter_by(email=email).first()

