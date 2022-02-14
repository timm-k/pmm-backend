import json
from pmm_backend import api
from pmm_backend.controllers.user import UserController
from pmm_backend.controllers.teams import TeamsController
from pmm_backend.controllers.employee import EmployeeController
from pmm_backend.controllers.team_role import TeamRolesController
from pmm_backend.controllers.workpackage import PackageController
from pmm_backend.controllers.session import SessionController
from pmm_backend.controllers.project import ProjectController
from flask import redirect, request, session, escape, jsonify
import time


@api.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'invalid url'}), 400


@api.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'message': 'request method not allowed'}), 405


##########################
# Users
##########################

@api.route('/user/list')
def list_users():
    return UserController.list_users()


@api.route('/user/login', methods=['POST'])
def login_user():
    return SessionController.login()


@api.route('/user', methods=['POST'])
def add_user():
    return UserController.add_user()


@api.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return UserController.update_user(user_id)


@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)


##########################
# Employees
##########################

@api.route('/employee/list')
def list_employees():
    return EmployeeController.list_employees()


@api.route('/employee/add', methods=['POST'])
def add_employee():
    first_name = escape(request.form.get('first_name'))
    last_name = escape(request.form.get('last_name'))

    EmployeeController.add_employee(first_name, last_name)
    return "True"


@api.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    first_name = request.form.get('first_name')
    if first_name is not None:
        first_name = escape(first_name)

    last_name = request.form.get('last_name')
    if last_name is not None:
        last_name = escape(last_name)

    EmployeeController.update_employee(employee_id, first_name, last_name)
    return "True"


@api.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    EmployeeController.delete_employee(employee_id)
    return "True"


##########################
# Teams
##########################

@api.route('/team/list')
def list_teams():
    return TeamsController.list_teams()


@api.route('/team', methods=['POST'])
def add_team():
    return TeamsController.add_team()


@api.route('/team/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    return TeamsController.update_team(team_id)


@api.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    return TeamsController.delete_team(team_id=team_id)


##########################
# Team Roles
##########################

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


##########################
# Projects
##########################

@api.route('/project/list')
def list_projects():
    return ProjectController.list_projects()


@api.route('/project/add', methods=['POST'])
def add_project():
    name = escape(request.form.get('name'))
    description = escape(request.form.get('description'))
    start_timestamp = int(time.time())
    end_timestamp = int(time.time())

    ProjectController.add_project(name, description, start_timestamp, end_timestamp)
    return "True"


@api.route('/project/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    start_timestamp = request.form.get('start_timestamp')
    if start_timestamp is not None:
        start_timestamp = escape(start_timestamp)

    end_timestamp = request.form.get('end_timestamp')
    if end_timestamp is not None:
        end_timestamp = escape(end_timestamp)

    ProjectController.update_project(project_id, name, description, start_timestamp, end_timestamp)
    return "True"


@api.route('/project/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    ProjectController.delete_project(project_id)
    return "True"


##########################
# Work-Package
##########################

@api.route('/package/list')
def list_package():
    return PackageController.list_packages()


@api.route('/package/add', methods=['POST'])
def add_package():
    project_id = escape(request.form.get('project_id'))
    name = escape(request.form.get('name'))
    description = escape(request.form.get('description'))
    start_timestamp = int(time.time())
    end_timestamp = int(time.time())

    PackageController.add_package(project_id, name, description, start_timestamp, end_timestamp)
    return "True"


@api.route('/package/<int:word_package_id>', methods=['PUT'])
def update_package(word_package_id):
    project_id = request.form.get('project_id')
    if project_id is not None:
        project_id = int(project_id)

    name = request.form.get('name')
    if name is not None:
        name = escape(name)

    description = request.form.get('description')
    if description is not None:
        description = escape(description)

    start_timestamp = request.form.get('start_timestamp')
    if start_timestamp is not None:
        start_timestamp = escape(start_timestamp)

    end_timestamp = request.form.get('end_timestamp')
    if end_timestamp is not None:
        end_timestamp = escape(end_timestamp)

    PackageController.update_package(word_package_id, project_id, name, description, start_timestamp, end_timestamp)
    return "True"


@api.route('/package/<int:word_package_id>', methods=['DELETE'])
def delete_package(word_package_id):
    PackageController.delete_package(word_package_id)
    return "True"
