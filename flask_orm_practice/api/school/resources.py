
from flask import request
from flask_restful import Resource, marshal

from api.school.structures import school_structure
from db import db, School


class SchoolResource(Resource):
    def get(self):
        return marshal(db.session.query(School).all(), school_structure)

    def post(self):
        data = request.json
        school = School(**data)
        db.session.add(school)
        db.session.commit()

        return marshal(db.session.query(School).first(), school_structure), 201
