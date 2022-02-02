from pmm_backend import api
from pmm_backend.controllers.user import UserController
from flask import redirect, request, session, escape


@api.route('/user/list')
def list_users():
    return UserController.list_users()

@api.route('/user/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    status = UserController.try_login()
    return status

@api.route('/user/add', methods=['POST'])
def add_user():
    role_id = int(request.form.get('role_id'))
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    first_name = escape(request.form.get('first_name'))
    last_name = escape(request.form.get('last_name'))

    status = UserController.add_user(role_id=role_id, email=email, password=password, first_name=first_name,
                                     last_name=last_name)
    return status