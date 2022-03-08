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

class RoutesController:

    @api.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'invalid url'}), 400


    @api.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({'message': 'request method not allowed'}), 405

    ##########################
    # Users
    ##########################

    @staticmethod
    @api.route('/user/list')
    def list_users():
        return UserController.list_users()

    @staticmethod
    @api.route('/user/login', methods=['POST'])
    def login_user():
        return SessionController.login()

    @staticmethod
    @api.route('/user', methods=['POST'])
    def add_user():
        return UserController.add_user()


    @staticmethod
    @api.route('/user/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        return UserController.update_user(user_id)

    @staticmethod
    @api.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        return UserController.delete_user(user_id)


    ##########################
    # Employees
    ##########################

    @staticmethod
    @api.route('/employee/list')
    def list_employees():
        return EmployeeController.list_employees()

    @staticmethod
    @api.route('/employee', methods=['POST'])
    def add_employee():
        return EmployeeController.add_employee()

    @staticmethod
    @api.route('/employee/<int:employee_id>', methods=['PUT'])
    def update_employee(employee_id):
        return EmployeeController.update_employee(employee_id)

    @staticmethod
    @api.route('/employee/<int:employee_id>', methods=['DELETE'])
    def delete_employee(employee_id):
        return EmployeeController.delete_employee(employee_id)


    ##########################
    # Teams
    ##########################

    @staticmethod
    @api.route('/team/list')
    def list_teams():
        return TeamsController.list_teams()

    @staticmethod
    @api.route('/team', methods=['POST'])
    def add_team():
        return TeamsController.add_team()

    @staticmethod
    @api.route('/team/<int:team_id>', methods=['PUT'])
    def update_team(team_id):
        return TeamsController.update_team(team_id)

    @staticmethod
    @api.route('/team/<int:team_id>', methods=['DELETE'])
    def delete_team(team_id):
        return TeamsController.delete_team(team_id=team_id)


    ##########################
    # Team Roles
    ##########################

    @staticmethod
    @api.route('/team/role/list')
    def list_team_roles():
        return TeamRolesController.list_team_roles()

    @staticmethod
    @api.route('/team/role', methods=['POST'])
    def add_team_role():
        return TeamRolesController.add_team_role()

    @staticmethod
    @api.route('/team/role/<int:team_role_id>', methods=['PUT'])
    def update_team_role(team_role_id):
        return TeamRolesController.update_team_role(team_role_id)


    @staticmethod
    @api.route('/team/role/<int:team_role_id>', methods=['DELETE'])
    def delete_team_role(team_role_id):
        return TeamRolesController.delete_team_role(team_role_id)


    ##########################
    # Projects
    ##########################

    @staticmethod
    @api.route('/project/list')
    def list_projects():
        return ProjectController.list_projects()


    @staticmethod
    @api.route('/project', methods=['POST'])
    def add_project():
        return ProjectController.add_project()

    @staticmethod
    @api.route('/project/<int:project_id>', methods=['PUT'])
    def update_project(project_id):
        return ProjectController.update_project(project_id)

    @staticmethod
    @api.route('/project/<int:project_id>', methods=['DELETE'])
    def delete_project(project_id):
        return ProjectController.delete_project(project_id)


    ##########################
    # Work-Package
    ##########################

    @staticmethod
    @api.route('/package/list')
    def list_package():
        return PackageController.list_packages()


    @staticmethod
    @api.route('/package/add', methods=['POST'])
    def add_package():
        return PackageController.add_package()


    @staticmethod
    @api.route('/package/<int:word_package_id>', methods=['PUT'])
    def update_package(word_package_id):
        return PackageController.update_package(word_package_id)

    @staticmethod
    @api.route('/package/<int:word_package_id>', methods=['DELETE'])
    def delete_package(word_package_id):
        return PackageController.delete_package(word_package_id)
