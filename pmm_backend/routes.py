import json

from pmm_backend import api
from pmm_backend.controllers.user import UserController
from pmm_backend.controllers.employee import EmployeeController
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


@api.route('/user', methods=['POST', 'PUT'])
def add_user():

    if not UserController.is_admin(session):
        return "no_permission"

    role_id = request.form.get('role_id')
    if role_id is not None:
        role_id = int(role_id)
    email = request.form.get('email')
    if email is not None:
        email = escape(email)
    password = request.form.get('password')
    if password is not None:
        password = escape(password)
    first_name = request.form.get('first_name')
    if first_name is not None:
        first_name = escape(first_name)
    last_name = request.form.get('last_name')
    if last_name is not None:
        last_name = escape(last_name)

    if request.method == 'POST':
        UserController.add_user(role_id=role_id, email=email, password=password, first_name=first_name,
                                         last_name=last_name)
        return "True"

    if request.method == 'PUT':
        user_id = int(request.form.get('user_id'))
        UserController.update_user(user_id=user_id, role_id=role_id, first_name=first_name, last_name=last_name,
                                    password=password, email=email)
        return "True"


@api.route('/employee/list')
def list_employees():
    return EmployeeController.list_employees()


@api.route('/employee/add', methods=['POST'])
def add_employee():
    first_name = escape(request.form.get('first_name'))
    last_name = escape(request.form.get('last_name'))

    status = EmployeeController.add_employee(first_name=first_name, last_name=last_name)
    return status


@api.route('/employee/<employee_id>', methods=['PUT'])
def update_employee():
    employee_id = request.form.get('employee_id')
    if employee_id is not None:
        employee_id = int(employee_id)

    first_name = request.form.get('first_name')
    if first_name is not None:
        first_name = escape(first_name)

    last_name = request.form.get('last_name')
    if last_name is not None:
        last_name = escape(last_name)

    status = EmployeeController.update_employee(employee_id=employee_id, first_name=first_name, last_name=last_name)
    return status


@api.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    status = EmployeeController.delete_employee(employee_id=employee_id)
    return status
