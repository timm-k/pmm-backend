from flask import jsonify, request, escape
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
    def add_user(**kwargs):
        user = models.User(email=escape(request.form.get('email')))

        role_id = request.form.get('role_id')
        if role_id is not None:
            user.role_id = int(role_id)

        password = request.form.get('password')
        if password is not None:
            bcrypt = Bcrypt(api)
            user.password_hash = bcrypt.generate_password_hash(password)

        first_name = request.form.get('first_name')
        if first_name is not None:
            user.first_name = escape(first_name)

        last_name = request.form.get('first_name')
        if last_name is not None:
            user.last_name = request.form.get('last_name')

        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.admin_required
    def update_user(user_id, role_id, email, password, first_name, last_name, **kwargs):
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
    def verify_login_valid(email, password, **kwargs):
        if models.User.query.filter_by(email=email).count() == 0:
            return False
        found_user = models.User.query.filter_by(email=email).first()

        bcrypt = Bcrypt(api)
        pass_valid = bcrypt.check_password_hash(found_user.password_hash, password)

        return pass_valid

    @staticmethod
    @SessionController.admin_required
    def try_login(session, email, password, **kwargs):
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
