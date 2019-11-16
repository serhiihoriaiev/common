from db import db

st_rooms = db.Table(
    'st_rooms',
    db.Column('st_id', db.String, db.ForeignKey('staff.pass_id')),
    db.Column('room_num', db.Integer, db.ForeignKey('room.number'))
)


class Staff(db.Model):
    pass_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float)
    rooms = db.relationship('Room', secondary=st_rooms, backref='staff')