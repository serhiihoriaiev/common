from flask_restful import fields

address_struct = {
    'addr_id': fields.Integer,
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

