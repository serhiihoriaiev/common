from flask_restful import fields, reqparse

ten_parser = reqparse.RequestParser()
ten_parser.add_argument('pass_id', type=str, required=True)
ten_parser.add_argument('name', type=str, required=True)
ten_parser.add_argument('age', type=int)
ten_parser.add_argument('sex', type=str)
ten_parser.add_argument('address', type=dict),
ten_parser.add_argument('room_num', type=int)

address_struct = {
    'country': fields.String,
    'city': fields.String,
    'stateprov': fields.String,
    'zip': fields.String,
    'street_addr': fields.String
}

ten_struct = {
    'pass_id': fields.String,
    'name': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_struct),
    'room_num': fields.Integer
}


class Tenant:
    def __init__(self, pass_id, name, age, sex, address, room_num):
        self.pass_id = pass_id
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
        self.room_num = room_num


ten_lst = [
    Tenant('14134fs2', 'Pedro Gonzalez', 23, 'male',
            {'country': 'Honduras', 'city': 'Tegucigalpa', 'stateprov': 'funduk',
             'zip': '666', 'street_addr': 'pr. Bandery, 23, apt. 4'}, 15),
    Tenant('14g5632', 'Margot Robbie', 27, 'female',
            {'country': 'Australia', 'city': 'Melburn', 'stateprov': 'Kenguru',
             'zip': '77778', 'street_addr': 'Unknown'}, 25)
]


