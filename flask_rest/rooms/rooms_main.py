import json

from flask import Blueprint, request
from flask_restful import Api, Resource, marshal, marshal_with
from rooms.res import Room, room_parser, r_struct, rooms_lst

rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)


class RoomsRes(Resource):
    def get(self):
        '''
        Get info about all rooms if no query string parameters added.
        Get info about particular rooms if '?number=' added
        Get info about all rooms with specified status if '?status=' added
        :return:
        '''
        if request.args.get('number'):
            data = [r for r in rooms_lst if r.number == int(request.args.get('number'))]
            return marshal(data[0], r_struct) if len(data) > 0 else None
        # get info by status
        if request.args.get('status'):
            data = [r for r in rooms_lst if r.status == request.args.get('status')]
            return marshal(data, r_struct) if len(data) > 0 else None
        return marshal(rooms_lst, r_struct)

    @marshal_with(r_struct)
    def post(self):
        '''
        Add a new room.
        :return:
        '''
        args = room_parser.parse_args()
        rooms_lst.append(Room(args['number'], args['level'], args['status'], args['price']))
        return rooms_lst

    @marshal_with(r_struct)
    def delete(self):
        '''
        Delete room by number.
        :return:
        '''
        rooms_lst[:] = [r for r in rooms_lst if r.number != int(request.args.get('number'))]
        return rooms_lst

    def patch(self):
        '''
        Update an existing room info.
        :return:
        '''
        args = room_parser.parse_args()
        if args['number'] in [r.number for r in rooms_lst]:
            pos = [r.number for r in rooms_lst].index(args['number'])
            rooms_lst[pos].level = args['level']
            rooms_lst[pos].status = args['status']
            rooms_lst[pos].price = args['price']
            return marshal(rooms_lst, r_struct)
        return json.loads('{"message": "No such room!"}')



api.add_resource(RoomsRes, '/rooms')