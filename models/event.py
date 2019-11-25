from . import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    menu = db.Column(db.String, nullable=False)
    date_created = db.column(db.DateTime)
    date_modified =db.column(db.DateTime)

    def __init__(self, title, menu, date_created, date_modified):
        self.title = title
        self.menu = menu
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # TODO Understand the update process
    def update(self, old, data):
        pass