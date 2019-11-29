from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class School(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    students = db.relationship('Student', backref='school')
    teachers = db.relationship('Teacher', backref='school')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    diary = db.relationship('Diary', backref='student', uselist=False)

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'),
                          nullable=False)


student_teacher = db.Table(
    'student_teacher',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    students = db.relationship('Student', secondary=student_teacher, backref='teachers')

class Diary(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))