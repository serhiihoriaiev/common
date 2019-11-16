from flask_restful import fields

r_struct = {'number': fields.Integer, 'level': fields.String, 'status': fields.String, 'price': fields.Float,
            'ten_id':fields.String}