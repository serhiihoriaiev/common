from flask_restful import fields, reqparse

staff_parser = reqparse.RequestParser()
staff_parser.add_argument('pass_id', type=str, required=True)
staff_parser.add_argument('name', type=str, required=True)
staff_parser.add_argument('position', type=str)
staff_parser.add_argument('salary', type=float)

staff_struct = {
    'pass_id': fields.String,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.Float
}


class Staff:
    def __init__(self, pass_id, name, position, salary):
        self.pass_id = pass_id
        self.name = name
        self.position = position
        self.salary = salary


staff_lst = [
    Staff('1234rw2', 'Konchita Ivanova', 'cleaner', 4300.0),
    Staff('534352r3', 'Vladislav Lox', 'security', 7500.0),
    Staff('432f24', 'Anzhela Olegovna', 'maid', 6800.0)
]


