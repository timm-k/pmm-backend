import json
from pmm_backend import api
from pmm_backend.controllers.user import UserController
from pmm_backend.controllers.teams import TeamsController
from pmm_backend.controllers.employee import EmployeeController
from pmm_backend.controllers.team_role import TeamRolesController
from flask import redirect, request, session, escape


@api.route('/user/list')
def list_users():
    return UserController.list_users()


@api.route('/user/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    status = UserController.try_login(session, email, password)
    return str(status)


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


@api.route('/team/list')
def list_teams():
    return TeamsController.list_teams()


@api.route('/team', methods=['POST'])
def add_team():
    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    TeamsController.add_team(name=name, description=description)
    return "True"


@api.route('/team/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    TeamsController.update_team(team_id=team_id, name=name, description=description)
    return "True"


@api.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    TeamsController.delete_team(team_id=team_id)
    return "True"


###########
# Team Roles
###########

@api.route('/team/role/list')
def list_team_roles():
    return TeamRolesController.list_team_roles()


@api.route('/team/role', methods=['POST'])
def add_team_role():
    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    TeamRolesController.add_team_role(name=name, description=description)
    return "True"


@api.route('/team/role/<int:team_role_id>', methods=['PUT'])
def update_team_role(team_role_id):
    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    TeamRolesController.update_team_role(team_role_id=team_role_id, name=name, description=description)
    return "True"


@api.route('/team/role/<int:team_role_id>', methods=['DELETE'])
def delete_team_role(team_role_id):
    TeamRolesController.delete_team_role(team_role_id=team_role_id)
    return "True"
