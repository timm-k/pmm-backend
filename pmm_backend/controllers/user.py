from sqlalchemy.ext.declarative import DeclarativeMeta
from pmm_backend import api
from pmm_backend.models import models
from flask_restx import Resource, fields, marshal
from flask_bcrypt import Bcrypt

import json


class UserController():
    @staticmethod
    def verify_login(email, password):
        if models.User.query.filter_by(email=email).count() == 0:
            return False

        found_user = models.User.query.filter_by(email=email).first()

        bcrypt = Bcrypt(api)
        pass_valid = bcrypt.check_password_hash(found_user.pass_hash, password)

        return json.dumps(pass_valid)

    def is_logged_in(self):
        pass

    def is_admin(self):
        pass

    @staticmethod
    def list_users():
        marshaller = {
            'user_id': fields.Integer,
            'role_id': fields.Integer,
            'email': fields.String,
            'first_name': fields.String,
            'last_name': fields.String,
        }

        found_users = models.User.query.all()
        return json.dumps(marshal(found_users, marshaller))
