import uuid
from flask import json
from proj.models import db


class User(db.Model):
    uuid = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(50))
    date_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(50))

    def __init__(self, name, age, date_birth, gender):
        self.uuid = uuid.uuid4().hex
        self.name = name
        self.age = age
        self.date_birth = date_birth
        self.gender = gender
