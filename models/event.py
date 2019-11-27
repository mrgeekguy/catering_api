from . import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    title = db.Column(db.String(50), nullable=False)
    menu = db.Column(db.String, nullable=False)
    event_date = db.Column(db.DateTime)
    date_created = db.column(db.DateTime)
    date_modified =db.column(db.DateTime)

    def __init__(self, title, menu, event_date, date_created, date_modified):
        self.title = title
        self.menu = menu
        self.event_date = event_date
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, event, event_change):
        for key, item in event_change.items():
            setattr(event, key, item
        self.last_modified = datetime.utcnow()
        db.session.commit()
        return event

    @staticmethod
    # gets single event
    def get_event(event_id):
        return Event.query.filter_by(id=event_id).first()

    @staticmethod
    # gets all events setup by client
    def get_all_events(client):
        return Event.query.filter_by(client_id=client)

    @staticmethod
    # gets event owner off event id
    def get_event_by_owner(event_id):
        return Event.query.filter_by(id=event_id).first().client_id

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    client_id = fields.Int(required=True, dump_only=True)
    title = fields.Str(dump_only=True)
    menu = fields.Str(dump_only=True)
    event_date = fields.DateTime(dump_only=True)
    

