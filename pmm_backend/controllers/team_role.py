from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal
import json


class TeamRolesController:
    @staticmethod
    def add_team_role(name, description):
        team_role = models.TeamRole(name=name, description=description)

        db.session.add(team_role)
        db.session.commit()

    @staticmethod
    def update_team_role(team_role_id, name, description):
        found_team_role = models.TeamRole.query.filter_by(team_role_id=team_role_id).first()

        if name is not None:
            found_team_role.name = name

        if description is not None:
            found_team_role.description = description

        db.session.commit()

    @staticmethod
    def delete_team_role(team_role_id):
        found_team_role = models.TeamRole.query.filter_by(team_role_id=team_role_id).first()
        db.session.delete(found_team_role)
        db.session.commit()

    @staticmethod
    def list_team_roles():
        marshaller = {
            'team_role_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
        }

        found_team_roles = models.TeamRole.query.all()
        return json.dumps(marshal(found_team_roles, marshaller))
