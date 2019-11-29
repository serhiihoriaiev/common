import json
from unittest import TestCase

from app import create_app
from db import db

app = create_app('TEST')


class SchoolTest(TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testPost(self):
        obj = {"name": "school_1"}
        test_req = app.test_client().post('/school', data=json.dumps(obj), content_type='application/json')

        self.assertEqual(201, test_req.status_code)
        self.assertEqual({"id": 1, "name": "school_1"}, test_req.json)
