from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True)
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<Book %s>' % self.title