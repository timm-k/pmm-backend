from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal

import json


class TeamsController:
    @staticmethod
    def add_team(name, description):
        team = models.Team(name=name, description=description)

        db.session.add(team)
        db.session.commit()

    @staticmethod
    def update_team(team_id, name, description):
        found_team = models.Team.query.filter_by(team_id=team_id).first()

        if name is not None:
            found_team.name = name

        if description is not None:
            found_team.description = description

        db.session.commit()

    @staticmethod
    def delete_team(team_id):
        found_team = models.Team.query.filter_by(team_id=team_id).first()
        db.session.delete(found_team)
        db.session.commit()

    @staticmethod
    def list_teams():
        marshaller = {
            'team_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
        }

        found_teams = models.Team.query.all()
        return json.dumps(marshal(found_teams, marshaller))
