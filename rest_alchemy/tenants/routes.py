import json

from flask import request
from flask_restful import Resource, marshal

from db import db
from models.tenant_model import Tenant, Address
from tenants.structure import ten_struct, address_struct


class TenantsRes(Resource):
    def get(self):
        '''
        Get particular tenant by pass_id if '?pass_id=' specified or
        get all tenants if not.
        :return:
        '''
        if request.args.get('pass_id'):
            data = db.session.query(Tenant).filter(Tenant.pass_id == request.args.get('pass_id')).first()
            return marshal(data, ten_struct) if data else "No such tenant!"
        elif not request.args:
            data = db.session.query(Tenant).all()
            return marshal(data, ten_struct)
        else:
            return "Unknown query"

    def post(self):
        '''
        Add new tenant to DB (without address)
        :return:
        '''
        data = json.loads(request.data)
        if db.session.query(Tenant).get(data['pass_id']):
            return "This tenant is in DB already!"
        new_record = Tenant(**data)
        db.session.add(new_record)
        db.session.commit()
        return "Tenant added"

    def delete(self):
        '''
        Delete tenant by pass_id
        :return:
        '''
        if request.args.get('pass_id'):
            data = db.session.query(Tenant).get(request.args.get('pass_id'))
            if data:
                db.session.delete(data)
                db.session.commit()
                return "Tenant deleted"
            return "No such tenant"
        return "No pass_id provided"

    def patch(self):
        '''
        Update an existing tenant info.
        :return:
        '''
        data = json.loads(request.data)
        ten = db.session.query(Tenant).filter(Tenant.pass_id == data['pass_id']) if 'pass_id' in data.keys() else None
        if ten and ten.first():
            ten.update(data)
            db.session.commit()
            return "Tenant info updated"
        elif ten and not ten.first():
            return "No such tenant"
        else:
            return "Provide pass_id!"

class AddrRes(Resource):
    def get(self):
        '''Get all addresses'''
        data = db.session.query(Address).all()
        return marshal(data, address_struct)

    def post(self):
        '''
        Add new address
        :return:
        '''
        data = json.loads(request.data)
        new_record = Address(**data)
        db.session.add(new_record)
        db.session.commit()
        return "Address added"
