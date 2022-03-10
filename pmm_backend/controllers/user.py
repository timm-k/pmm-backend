"""
    Implements the UserController
"""
import json
from flask import jsonify, request, escape
from flask_restx import fields, marshal
from flask_bcrypt import Bcrypt

from pmm_backend import api, db
from pmm_backend.models import models
from pmm_backend.controllers.session import SessionController


class UserController():
    """
        User Controller Class
    """

    @staticmethod
    @SessionController.admin_required
    def add_user():
        """
        Adds a new user6.
        :return: Status in JSON format
        """
        email = request.form.get('email')
        if email is None:
            return jsonify({'message': 'missing data: email'}), 400
        email = str(escape(email))
        user = models.User(email=email)

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

        last_name = request.form.get('last_name')
        if last_name is not None:
            user.last_name = str(escape(request.form.get('last_name')))

        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'success', 'user_id': user.user_id}), 200

    @staticmethod
    @SessionController.admin_required
    def update_user(user_id):
        """
        Updates an existing user.
        :return: Status in JSON format
        """
        user = models.User.query.filter_by(user_id=user_id).first()

        if user is None:
            return jsonify({'message': 'user not found'}), 404

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

        last_name = request.form.get('last_name')
        if last_name is not None:
            user.last_name = request.form.get('last_name')

        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.admin_required
    def list_users():
        """
        Lists all users.
        :return: List of users in JSON format
        """
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
    def delete_user(user_id):
        """
        Deletes a user.
        :return: Status in JSON format
        """
        found_user = models.User.query.filter_by(user_id=user_id).first()

        if found_user is None:
            return jsonify({'message': 'user not found'}), 404

        db.session.delete(found_user)
        db.session.commit()
        return jsonify({'message': 'success'}), 200
