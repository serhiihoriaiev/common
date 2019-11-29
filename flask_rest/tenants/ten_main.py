import json

from flask import Blueprint, request
from flask_restful import Api, Resource, marshal, marshal_with

from tenants.res import ten_lst, ten_struct, ten_parser

ten_bp = Blueprint('tenants', __name__)
api = Api(ten_bp)


class TenRes(Resource):
    def get(self):
        '''
        Get particular tenant by pass_id if '?pass_id=' specified or
        get all tenants if not.
        :return:
        '''
        if request.args.get('pass_id'):
            data = [t for t in ten_lst if t.pass_id == request.args.get('pass_id')]
            return marshal(data[0], ten_struct) if len(data) > 0 else None
        return marshal(ten_lst, ten_struct)

    @marshal_with(ten_struct)
    def delete(self):
        '''
        Delete tenant by pass ID
        :return:
        '''
        ten_lst[:] = [t for t in ten_lst if t.pass_id != request.args.get('pass_id')]
        return ten_lst

    def patch(self):
        '''
        Update information about tenant if specified pass id exists in tenant list
        :return:
        '''
        args = ten_parser.parse_args()
        if args['pass_id'] in [t.pass_id for t in ten_lst]:
            pos = [r.pass_id for r in ten_lst].index(args['pass_id'])
            ten_lst[pos].name = args['name']
            ten_lst[pos].age = args['age']
            ten_lst[pos].sex = args['sex']
            ten_lst[pos].address = args['address']
            ten_lst[pos].room_num = args['room_num']
            return marshal(ten_lst, ten_struct)
        return json.loads('{"message": "No such tenant!"}')


api.add_resource(TenRes, '/tenants')
