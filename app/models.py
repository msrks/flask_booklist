from datetime import datetime
from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    # when_added = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    who_added = db.Column(db.String(30), index=True, default='shinzo_abe')

    def __repr__(self):
        return '<Book %s>' % self.title