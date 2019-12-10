from flask import Blueprint
from flask_restful import Api

from tenants.routes import TenantsRes, AddrRes

tenants_bp = Blueprint('tenants', __name__)
ten_api = Api(tenants_bp)

ten_api.add_resource(TenantsRes, '/tenants')
ten_api.add_resource(AddrRes, '/address')