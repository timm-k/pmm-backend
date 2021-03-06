"""
    Implements the TeamRolesController
"""
import json
from flask_restx import fields, marshal
from flask import jsonify, request, escape

from pmm_backend import db
from pmm_backend.models import models
from pmm_backend.controllers.session import SessionController


class TeamRolesController:
    """
        Team Roles Controller Class
    """
    @staticmethod
    @SessionController.login_required
    def add_team_role():
        """
        Adds a new team role.
        :return: Status in JSON format
        """
        name = request.form.get('name')
        description = request.form.get('description')

        if name is None:
            return jsonify({'message': 'missing data: name'}), 400
        if description is None:
            return jsonify({'message': 'missing data: description'}), 400

        name = escape(name)
        description = escape(description)
        team_role = models.TeamRole(name=name, description=description)

        db.session.add(team_role)
        db.session.commit()
        return jsonify({'message': 'success', 'team_role_id': team_role.team_role_id}), 200

    @staticmethod
    @SessionController.login_required
    def update_team_role(team_role_id):
        """
        Updates an existing team role.
        :return: Status in JSON format
        """
        found_team_role = models.TeamRole.query.filter_by(team_role_id=team_role_id).first()

        if found_team_role is None:
            return jsonify({'message': 'team role not found'}), 404

        name = request.form.get('name')
        description = request.form.get('description')

        if name is not None:
            found_team_role.name = escape(name)
        if description is not None:
            found_team_role.description = escape(description)

        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def delete_team_role(team_role_id):
        """
        Deletes a team role.
        :return: Status in JSON format
        """
        found_team_role = models.TeamRole.query.filter_by(team_role_id=team_role_id).first()

        if found_team_role is None:
            return jsonify({'message': 'team role not found'}), 404

        db.session.delete(found_team_role)
        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def list_team_roles():
        """
        Lists all team roles.
        :return: List of team roles in JSON format
        """
        marshaller = {
            'team_role_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
        }

        found_team_roles = models.TeamRole.query.all()
        return json.dumps(marshal(found_team_roles, marshaller))
