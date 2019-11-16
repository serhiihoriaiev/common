from flask import Blueprint
from flask_restful import Api

from staff.routes import StaffRes

staff_bp = Blueprint('staff', __name__)
staff_api = Api(staff_bp)

staff_api.add_resource(StaffRes, '/staff')