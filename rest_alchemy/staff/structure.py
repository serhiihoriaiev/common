from flask_restful import fields

staff_struct = {
    'pass_id': fields.String,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.Float
}