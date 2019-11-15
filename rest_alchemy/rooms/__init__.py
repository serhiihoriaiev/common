from flask import Blueprint
from flask_restful import Api

from rooms.routes import RoomsRes

rooms_bp = Blueprint('rooms', __name__)
rooms_api = Api(rooms_bp)

rooms_api.add_resource(RoomsRes, '/rooms')