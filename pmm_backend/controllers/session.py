from flask import jsonify, request, make_response
from flask_bcrypt import Bcrypt

from pmm_backend import api, settings, db
from pmm_backend.models import models
import time
import jwt
from functools import wraps

class SessionController():

    @staticmethod
    def login():
        # creates dictionary of form data
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

    def login_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
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
            return f(current_user=current_user, *args, **kwargs)
        return decorated

    def admin_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
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

            except Exception as e:
                print(e)
                return "invalid token", 401
            # returns the current logged in users contex to the routes
            return f(current_user=current_user, *args, **kwargs)
        return decorated