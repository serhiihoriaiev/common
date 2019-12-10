import json

from flask import Blueprint, request
from flask_restful import Api, Resource, marshal, marshal_with

from staff.res import staff_lst, staff_struct, staff_parser

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)


class StaffRes(Resource):
    def get(self):
        '''
        Get particular staff by pass_id if '?pass_id=' specified or
        get all staff if not.
        :return:
        '''
        if request.args.get('pass_id'):
            data = [t for t in staff_lst if t.pass_id == request.args.get('pass_id')]
            return marshal(data[0], staff_struct) if len(data) > 0 else None
        return marshal(staff_lst, staff_struct)

    @marshal_with(staff_struct)
    def delete(self):
        '''
        Delete staff by pass ID
        :return:
        '''
        staff_lst[:] = [t for t in staff_lst if t.pass_id != request.args.get('pass_id')]
        return staff_lst

    def patch(self):
        '''
        Update information about staff if specified pass id exists in tenant list
        :return:
        '''
        args = staff_parser.parse_args()
        if args['pass_id'] in [t.pass_id for t in staff_lst]:
            pos = [r.pass_id for r in staff_lst].index(args['pass_id'])
            staff_lst[pos].name = args['name']
            staff_lst[pos].position = args['position']
            staff_lst[pos].salary = args['salary']
            return marshal(staff_lst, staff_struct)
        return json.loads('{"message": "No such staff!"}')


api.add_resource(StaffRes, '/staff')
