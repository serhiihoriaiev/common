from flask_restful import reqparse, fields

room_parser = reqparse.RequestParser()
room_parser.add_argument('number', type=int, required=True)
room_parser.add_argument('level', type=str, required=True)
room_parser.add_argument('status', type=str, required=True)
room_parser.add_argument('price', type=float, required=True)


class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_lst = [
    Room(7, 'utils', 'closed', 0.0),
    Room(12, 'econom', 'available', 50.0),
    Room(15, 'base', 'occupied', 75.0),
    Room(25, 'business', 'occupied', 100.0)
]

r_struct = {'number': fields.Integer, 'level': fields.String, 'status': fields.String, 'price': fields.Float}
