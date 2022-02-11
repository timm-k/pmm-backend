from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal


import json


class ProjectController:

    @staticmethod
    def list_projects():
        marshaller = {
            'project_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
            'start_timestamp': fields.Integer,
            'end_timestamp': fields.Integer,
        }

        all_projects = models.Project.query.all()
        return json.dumps(marshal(all_projects, marshaller))

    @staticmethod
    def add_project(name, description, start_timestamp, end_timestamp):
        project = models.Project(name=name, description=description,
                                 start_timestamp=start_timestamp, end_timestamp=end_timestamp)

        db.session.add(project)
        db.session.commit()

    @staticmethod
    def update_project(project_id, name, description, start_timestamp, end_timestamp):
        project = models.Project.query.filter_by(project_id=project_id)

        if name is not None:
            project.name = name
        if description is not None:
            project.description = description
        if start_timestamp is not None:
            project.start_timestamp = start_timestamp
        if end_timestamp is not None:
            project.end_timestamp = end_timestamp

        db.session.commit()

    @staticmethod
    def delete_project(project_id):
        models.Project.query.filter_by(project_id=project_id).delete()
        db.session.commit()


