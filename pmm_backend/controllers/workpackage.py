from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal

import json


class PackageController:

    @staticmethod
    def list_packages():
        marshaller = {
            'project_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
            'start_timestamp': fields.Integer,
            'end_timestamp': fields.Integer,
        }

        all_packages = models.WorkPackage.query.all()
        return json.dumps(marshal(all_packages, marshaller))

    @staticmethod
    def add_package(project_id, name, description, start_timestamp, end_timestamp):
        package = models.WorkPackage(project_id=project_id, name=name, description=description,
                                     start_timestamp=start_timestamp, end_timestamp=end_timestamp)

        db.session.add(package)
        db.session.commit()

    @staticmethod
    def update_package(word_package_id, project_id, name, description, start_timestamp, end_timestamp):
        package = models.WorkPackage.query.filter_by(word_package_id=word_package_id).first()

        if project_id is not None:
            package.project_id = project_id
        if name is not None:
            package.name = name
        if description is not None:
            package.description = description
        if start_timestamp is not None:
            package.start_timestamp = start_timestamp
        if end_timestamp is not None:
            package.end_timestamp = end_timestamp

        db.session.commit()

    @staticmethod
    def delete_package(word_package_id):
        models.WorkPackage.query.filter_by(word_package_id=word_package_id).delete()
        db.session.commit()