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
def modify_employee():
    first_name = escape(request.form.get('first_name'))
    last_name = escape(request.form.get('last_name'))

    status = EmployeeController.modify_employee(first_name=first_name, last_name=last_name)
    return status


@api.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    status = EmployeeController.delete_employee(employee_id=employee_id)
    return status
