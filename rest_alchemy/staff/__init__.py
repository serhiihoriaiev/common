from flask import Blueprint
from flask_restful import Api

from staff.routes import StaffRes, StaffRoomsRes

staff_bp = Blueprint('staff', __name__)
staff_api = Api(staff_bp)

staff_api.add_resource(StaffRes, '/staff')
staff_api.add_resource(StaffRoomsRes, '/staff_room')