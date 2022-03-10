"""
    Implements the RoutesController which defines all API routes.
"""
from flask import jsonify

from pmm_backend import api
from pmm_backend.controllers.user import UserController
from pmm_backend.controllers.teams import TeamsController
from pmm_backend.controllers.employee import EmployeeController
from pmm_backend.controllers.team_role import TeamRolesController
from pmm_backend.controllers.workpackage import PackageController
from pmm_backend.controllers.session import SessionController
from pmm_backend.controllers.project import ProjectController


class RoutesController:
    """
        Routes Controller Class
    """

    @staticmethod
    @api.errorhandler(404)
    def page_not_found():
        """Adds a custom errorhandler for 404 errors."""
        return jsonify({'message': 'invalid url'}), 400

    @staticmethod
    @api.errorhandler(405)
    def method_not_allowed():
        """Adds a custom errorhandler for 405 errors."""
        return jsonify({'message': 'request method not allowed'}), 405

    ##########################
    # Users
    ##########################

    @staticmethod
    @api.route('/user/list')
    def list_users():
        """Adds a route for listing users."""
        return UserController.list_users()

    @staticmethod
    @api.route('/user/login', methods=['POST'])
    def login_user():
        """Adds a route for user login."""
        return SessionController.login()

    @staticmethod
    @api.route('/user', methods=['POST'])
    def add_user():
        """Adds a route for adding users."""
        return UserController.add_user()

    @staticmethod
    @api.route('/user/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        """Adds a route for updating users."""
        return UserController.update_user(user_id)

    @staticmethod
    @api.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        """Adds a route for deleting users."""
        return UserController.delete_user(user_id)

    ##########################
    # Employees
    ##########################

    @staticmethod
    @api.route('/employee/list')
    def list_employees():
        """Adds a route for listing employees."""
        return EmployeeController.list_employees()

    @staticmethod
    @api.route('/employee', methods=['POST'])
    def add_employee():
        """Adds a route for adding employees."""
        return EmployeeController.add_employee()

    @staticmethod
    @api.route('/employee/<int:employee_id>', methods=['PUT'])
    def update_employee(employee_id):
        """Adds a route for updating employees."""
        return EmployeeController.update_employee(employee_id)

    @staticmethod
    @api.route('/employee/<int:employee_id>', methods=['DELETE'])
    def delete_employee(employee_id):
        """Adds a route for deleting employees."""
        return EmployeeController.delete_employee(employee_id)

    ##########################
    # Teams
    ##########################

    @staticmethod
    @api.route('/team/list')
    def list_teams():
        """Adds a route for listing teams."""
        return TeamsController.list_teams()

    @staticmethod
    @api.route('/team', methods=['POST'])
    def add_team():
        """Adds a route for adding teams."""
        return TeamsController.add_team()

    @staticmethod
    @api.route('/team/<int:team_id>', methods=['PUT'])
    def update_team(team_id):
        """Adds a route for updating teams."""
        return TeamsController.update_team(team_id)

    @staticmethod
    @api.route('/team/<int:team_id>', methods=['DELETE'])
    def delete_team(team_id):
        """Adds a route for deleting teams."""
        return TeamsController.delete_team(team_id)

    ##########################
    # Team Roles
    ##########################

    @staticmethod
    @api.route('/team/role/list')
    def list_team_roles():
        """Adds a route for listing team roles."""
        return TeamRolesController.list_team_roles()

    @staticmethod
    @api.route('/team/role', methods=['POST'])
    def add_team_role():
        """Adds a route for adding team roles."""
        return TeamRolesController.add_team_role()

    @staticmethod
    @api.route('/team/role/<int:team_role_id>', methods=['PUT'])
    def update_team_role(team_role_id):
        """Adds a route for updating team roles."""
        return TeamRolesController.update_team_role(team_role_id)

    @staticmethod
    @api.route('/team/role/<int:team_role_id>', methods=['DELETE'])
    def delete_team_role(team_role_id):
        """Adds a route for deleing team roles."""
        return TeamRolesController.delete_team_role(team_role_id)

    ##########################
    # Projects
    ##########################

    @staticmethod
    @api.route('/project/list')
    def list_projects():
        """Adds a route for listing projects."""
        return ProjectController.list_projects()

    @staticmethod
    @api.route('/project', methods=['POST'])
    def add_project():
        """Adds a route for adding projects."""
        return ProjectController.add_project()

    @staticmethod
    @api.route('/project/<int:project_id>', methods=['PUT'])
    def update_project(project_id):
        """Adds a route for updating projects."""
        return ProjectController.update_project(project_id)

    @staticmethod
    @api.route('/project/<int:project_id>', methods=['DELETE'])
    def delete_project(project_id):
        """Adds a route for deleting projects."""
        return ProjectController.delete_project(project_id)

    ##########################
    # Work-Package
    ##########################

    @staticmethod
    @api.route('/package/list')
    def list_package():
        """Adds a route for listing work packages."""
        return PackageController.list_packages()

    @staticmethod
    @api.route('/package', methods=['POST'])
    def add_package():
        """Adds a route for adding work packages."""
        return PackageController.add_package()

    @staticmethod
    @api.route('/package/<int:word_package_id>', methods=['PUT'])
    def update_package(word_package_id):
        """Adds a route for updating work packages."""
        return PackageController.update_package(word_package_id)

    @staticmethod
    @api.route('/package/<int:word_package_id>', methods=['DELETE'])
    def delete_package(word_package_id):
        """Adds a route for deleting work packages."""
        return PackageController.delete_package(word_package_id)
