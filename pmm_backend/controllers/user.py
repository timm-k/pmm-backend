from sqlalchemy.ext.declarative import DeclarativeMeta
from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import Resource, fields, marshal
from flask_bcrypt import Bcrypt
import time
import json


class UserController():
    @staticmethod
    def add_user(role_id, email, password, first_name, last_name):
        bcrypt = Bcrypt(api)
        hash = bcrypt.generate_password_hash(password)

        user = models.User(role_id=role_id, email=email, first_name=first_name,
                           last_name=last_name, password_hash=hash)

        db.session.add(user)
        db.session.commit()

    @staticmethod
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
    def verify_login_valid(email, password):
        if models.User.query.filter_by(email=email).count() == 0:
            return False
        found_user = models.User.query.filter_by(email=email).first()

        bcrypt = Bcrypt(api)
        pass_valid = bcrypt.check_password_hash(found_user.password_hash, password)

        return pass_valid

    @staticmethod
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
    def is_logged_in(session):
        return True # REMOVE BEFORE RELEASE !

        if 'user_id' not in session:
            return False

        expire_timestamp = session['session_expire_timestamp']
        current_timestamp = int(time.time())

        if current_timestamp > expire_timestamp:
            return False

        return True

    @staticmethod
    def is_admin(session):
        return True # REMOVE BEFORE RELEASE !

        if not UserController.is_logged_in(session):
            return False

        user_id = session['user_id']
        found_user = models.User.query.filter_by(user_id=user_id).first()
        role_id = found_user.role_id

        if role_id == 1:
            return True
        return False

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
