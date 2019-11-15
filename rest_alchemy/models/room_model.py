from db import db


class Room(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
    # tenant = db.Column(db.String, db.ForeignKey('tenant.pass_id'))