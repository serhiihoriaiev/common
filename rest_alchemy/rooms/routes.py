import json

from flask import request
from flask_restful import Resource, marshal

from db import db
from models.room_model import Room
from rooms.structure import r_struct


class RoomsRes(Resource):
    def get(self):
        '''
        Get info about all rooms if no query string parameters added.
        Get info about particular rooms if '?number=' added
        Get info about all rooms with specified status if '?status=' added
        :return:
        '''
        if request.args.get('number'):
            data = db.session.query(Room).filter(Room.number == request.args.get('number')).first()
            return marshal(data, r_struct) if data else "No such room!"
        if request.args.get('status'):
            data = db.session.query(Room).filter(Room.status == request.args.get('status')).all()
            return marshal(data, r_struct) if data else "No such room!"
        elif not request.args:
            data = db.session.query(Room).all()
            return marshal(data, r_struct)
        else:
            return "Unknown query"

    def post(self):
        '''
        Add a new room.
        :return:
        '''
        data = json.loads(request.data)
        if db.session.query(Room).filter(Room.number == data['number']).first():
            return "This room is in DB already"
        new_record = Room(**data)
        db.session.add(new_record)
        db.session.commit()
        return "New record added"

    def delete(self):
        '''
        Delete room by number.
        :return:
        '''
        if request.args.get('number'):
            data = db.session.query(Room).filter(Room.number == request.args.get('number')).first()
            if data:
                db.session.delete(data)
                db.session.commit()
                return "Room deleted"
            return "No such room"
        return "No number provided"

    def patch(self):
        '''
        Update an existing room info.
        :return:
        '''
        data = json.loads(request.data)
        room = db.session.query(Room).filter(Room.number == data['number']) if 'number' in data.keys() else None
        if room and room.first():
            room.update(data)
            db.session.commit()
            return "Room updated"
        elif room and not room.first():
            return "No such room"
        else:
            return "Provide room number!"
