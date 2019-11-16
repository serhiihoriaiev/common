import json

from flask import request
from flask_restful import Resource, marshal

from db import db
from models.room_model import Room
from models.staff_model import Staff
from staff.structure import staff_struct


class StaffRes(Resource):
    def get(self):
        '''
        Get particular staff by pass_id if '?pass_id=' specified or
        get all staff if not.
        :return:
        '''
        if request.args.get('pass_id'):
            data = db.session.query(Staff).get(request.args.get('pass_id'))
            return marshal(data, staff_struct) if data else "No such staff!"
        elif not request.args:
            data = db.session.query(Staff).all()
            return marshal(data, staff_struct)
        else:
            return "Unknown query"

    def post(self):
        '''
        Add new staff to DB.
        :return:
        '''
        data = json.loads(request.data)
        if db.session.query(Staff).get(data['pass_id']):
            return "This staff is in DB already!"
        new_record = Staff(**data)
        db.session.add(new_record)
        db.session.commit()
        return "Staff added to DB"

    def delete(self):
        '''
        Delete staff by pass_id
        :return:
        '''
        if request.args.get('pass_id'):
            data = db.session.query(Staff).get(request.args.get('pass_id'))
            if data:
                db.session.delete(data)
                db.session.commit()
                return "Staff deleted"
            return "No such staff!"
        return "Provide pass_id!"

    def patch(self):
        '''
        Update an existing staff info.
        :return:
        '''
        data = json.loads(request.data)
        st = db.session.query(Staff).filter(Staff.pass_id == data['pass_id']) if 'pass_id' in data.keys() else None
        if st and st.first():
            st.update(data)
            db.session.commit()
            return "Staff info modified"
        elif st and not st.first():
            return "No such staff!"
        else:
            return "Provide pass_id!"

class StaffRoomsRes(Resource):
    def post(self):
        '''
        Add a room to staff
        :return:
        '''
        data = json.loads(request.data)
        if data['st_id'] and data['room_num']:
            staff = db.session.query(Staff).get(data['st_id'])
            room = db.session.query(Room).get(data['room_num'])
            staff.rooms.append(room)
            db.session.commit()
            return f'Room {room.number} added to {staff.name}'
        return 'Invalid POST body'