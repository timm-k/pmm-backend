from flask import jsonify
from sqlalchemy.ext.declarative import DeclarativeMeta
from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import Resource, fields, marshal
from flask_bcrypt import Bcrypt
import time
import json
from pmm_backend.controllers.session import SessionController


class UserController():

    @staticmethod
    @SessionController.admin_required
    def add_user(role_id, email, password, first_name, last_name):
        bcrypt = Bcrypt(api)
        hash = bcrypt.generate_password_hash(password)

        user = models.User(role_id=role_id, email=email, first_name=first_name,
                           last_name=last_name, password_hash=hash)

        db.session.add(user)
        db.session.commit()

    @staticmethod
    @SessionController.admin_required
    def update_user(user_id, role_id, email, password, first_name, last_name):
        found_user = models.User.query.filter_by(user_id=user_id).first()

        if role_id is not None:
            found_user.role_id = role_id

        if email is not None:
            found_user.email = email

        if first_name is not None:
            found_user.first_name = first_name

        if last_name is not None:
            found_user.last_name = last_name

        if password is not None:
            bcrypt = Bcrypt(api)
            hash = bcrypt.generate_password_hash(password)
            found_user.password_hash = hash

        db.session.commit()

    @staticmethod
    @SessionController.admin_required
    def verify_login_valid(email, password):
        if models.User.query.filter_by(email=email).count() == 0:
            return False
        found_user = models.User.query.filter_by(email=email).first()

        bcrypt = Bcrypt(api)
        pass_valid = bcrypt.check_password_hash(found_user.password_hash, password)

        return pass_valid

    @staticmethod
    @SessionController.admin_required
    def try_login(session, email, password):
        login_valid = UserController.verify_login_valid(email, password)

        if login_valid:
            found_user = models.User.query.filter_by(email=email).first()

            user_id = found_user.user_id
            session['user_id'] = user_id
            session['session_expire_timestamp'] = int(time.time()) + settings.SESSION_TIMEOUT
            return True
        else:
            return False

    @staticmethod
    @SessionController.admin_required
    def list_users(**kwargs):
        marshaller = {
            'user_id': fields.Integer,
            'role_id': fields.Integer,
            'email': fields.String,
            'first_name': fields.String,
            'last_name': fields.String,
        }

        found_users = models.User.query.all()
        return json.dumps(marshal(found_users, marshaller))
