from pmm_backend.controllers.session import SessionController
from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal
from flask import jsonify, request, escape
import json
from pmm_backend.controllers.session import SessionController


class TeamsController:
    @staticmethod
    @SessionController.login_required
    def add_team(**kwargs):
        name = request.form.get('name')
        description = request.form.get('description')

        if name is None:
            return jsonify({'message': 'missing data: name'}), 400
        if description is None:
            return jsonify({'message': 'missing data: description'}), 400

        name = escape(name)
        description = escape(description)
        team = models.Team(name=name, description=description)

        db.session.add(team)
        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def update_team(team_id, **kwargs):
        found_team = models.Team.query.filter_by(team_id=team_id).first()

        if found_team is None:
            return jsonify({'message': 'team not found'}), 404

        name = request.form.get('name')
        description = request.form.get('description')

        if name is not None:
            found_team.name = escape(name)
        if description is not None:
            found_team.description = escape(description)

        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def delete_team(team_id, **kwargs):
        found_team = models.Team.query.filter_by(team_id=team_id).first()

        if found_team is None:
            return jsonify({'message': 'team not found'}), 404

        db.session.delete(found_team)
        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def list_teams(**kwargs):
        marshaller = {
            'team_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
        }

        found_teams = models.Team.query.all()
        return json.dumps(marshal(found_teams, marshaller))
