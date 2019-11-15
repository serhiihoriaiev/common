from db import db


class Tenant(db.Model):
    pass_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    addr_id = db.Column(db.ForeignKey('address.addr_id'), default=None)
    room_num = db.Column(db.Integer)
    # rooms = db.relationship('Room', backref='tenant')


class Address(db.Model):
    addr_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    stateprov = db.Column(db.String)
    zip = db.Column(db.String)
    street_addr = db.Column(db.String)
    residents = db.relationship('Tenant', backref='address')
