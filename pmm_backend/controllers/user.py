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
            user.password_hash = str(bcrypt.generate_password_hash(password))

        first_name = request.form.get('first_name')
        if first_name is not None:
            user.first_name = str(escape(first_name))

        last_name = request.form.get('first_name')
        if last_name is not None:
            user.last_name = str(escape(request.form.get('last_name')))

        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.admin_required
    def update_user(user_id, **kwargs):
        user = models.User.query.filter_by(user_id=user_id).first()

        role_id = request.form.get('role_id')
        if role_id is not None:
            user.role_id = int(role_id)

        email = request.form.get('email')
        if email is not None:
            user.email = escape(email)

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

        db.session.commit()
        return jsonify({'message': 'success'}), 200

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

    @staticmethod
    @SessionController.admin_required
    def delete_user(user_id, **kwargs):
        found_user = models.User.query.filter_by(user_id=user_id).first()
        db.session.delete(found_user)
        db.session.commit()
        return jsonify({'message': 'success'}), 200