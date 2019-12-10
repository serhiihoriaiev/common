from flask_restful import fields

from rooms.structure import r_struct

staff_struct = {
    'pass_id': fields.String,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.Float,
    'rooms': fields.Nested(r_struct)
}