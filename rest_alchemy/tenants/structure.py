from flask_restful import fields

from rooms.structure import r_struct

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
    'addr_id': fields.Integer,
    'address': fields.Nested(address_struct),
    'rooms': fields.Nested(r_struct)
}

