"""
    Implements the SessionController
"""
import time
from functools import wraps
import jwt
from flask import jsonify, request
from flask_bcrypt import Bcrypt

from pmm_backend import api, settings
from pmm_backend.models import models


class SessionController():
    """
        Session Controller Class
    """
    @staticmethod
    def login():
        """
        Try to login with the given data.
        :return: Login status and token in JSON format
        """
        form_data = request.form

        if not form_data or not form_data.get('email') or not form_data.get('password'):
            return jsonify({'message': 'invalid login data'}), 401

        email = form_data.get('email')
        if models.User.query.filter_by(email=email).count() == 0:
            return jsonify({'message': 'invalid login data'}), 401

        found_user = models.User.query.filter_by(email=email).first()

        bcrypt = Bcrypt(api)
        password = form_data.get('password')
        pass_valid = bcrypt.check_password_hash(found_user.password_hash, password)

        if pass_valid:
            # generate token
            token = jwt.encode({
                'user_id': found_user.user_id,
                'expire_timestamp': int(time.time() + settings.SESSION_TIMEOUT)
            }, api.config['SECRET_KEY'])

            return jsonify({
                'message': 'success',
                'token': token
            }), 200

        return jsonify({'message': 'invalid password'}), 401

    @staticmethod
    def login_required(f):
        """
        Requires a valid login
        """
        @wraps(f)
        def decorated(*args):
            token = None
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            # return 401 if token is not passed
            if not token:
                return jsonify({'message': 'unauthorized'}), 401

            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, api.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = models.User.query.filter_by(user_id=data['user_id']).first()

                expire_timestamp = data['expire_timestamp']
                current_timestamp = int(time.time())
                if current_timestamp > expire_timestamp:
                    return jsonify({'message': 'invalid token'}), 401

            except:
                return jsonify({'message': 'invalid token'}), 401
            # returns the current logged in users contex to the routes
            return f(*args)

        return decorated

    @staticmethod
    def admin_required(f):
        """
        Requires a valid admin login
        """
        @wraps(f)
        def decorated(*args):
            token = None
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            # return 401 if token is not passed
            if not token:
                return jsonify({'message': 'unauthorized'}), 401

            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, api.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = models.User.query.filter_by(user_id=data['user_id']).first()

                expire_timestamp = data['expire_timestamp']
                current_timestamp = int(time.time())
                if current_timestamp > expire_timestamp:
                    return jsonify({'message': 'invalid token'}), 401

            except Exception:
                return "invalid token", 401
            # returns the current logged in users contex to the routes
            return f(*args)

        return decorated
