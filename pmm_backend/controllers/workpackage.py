import json
from flask_restx import fields, marshal
from flask import jsonify, request, escape

from pmm_backend import db
from pmm_backend.models import models
from pmm_backend.controllers.session import SessionController


class PackageController:

    @staticmethod
    @SessionController.login_required
    def list_packages(**kwargs):
        marshaller = {
            'work_package_id': fields.Integer,
            'project_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
            'start_timestamp': fields.Integer,
            'end_timestamp': fields.Integer,
        }

        all_packages = models.WorkPackage.query.all()
        return json.dumps(marshal(all_packages, marshaller))

    @staticmethod
    @SessionController.login_required
    def add_package(**kwargs):

        project_id = request.form.get('project_id')
        name = request.form.get('name')
        description = request.form.get('description')
        start_timestamp = request.form.get('start_timestamp')
        end_timestamp = request.form.get('end_timestamp')

        control_project_id = db.session.query(models.Project).filter(models.Project.project_id == project_id)

        if project_id is None:
            return jsonify({'message': 'missing data: project_id'}), 400
        if control_project_id.count() == 0:
            return jsonify({'message': 'project_id doesnt exists'}), 400
        if name is None:
            return jsonify({'message': 'missing data: name'}), 400
        if description is None:
            return jsonify({'message': 'missing data: description'}), 400
        if start_timestamp is None:
            return jsonify({'message': 'missing data: start_timestamp'}), 400
        if end_timestamp is None:
            return jsonify({'message': 'missing data: end_timestamp'}), 400

        project_id = int(project_id)
        name = escape(name)
        description = escape(description)
        start_timestamp = int(start_timestamp)
        end_timestamp = int(end_timestamp)

        package = models.WorkPackage(project_id=project_id, name=name, description=description,
                                     start_timestamp=start_timestamp, end_timestamp=end_timestamp)

        db.session.add(package)
        db.session.commit()
        return jsonify({'message': 'success', 'work_package_id': package.work_package_id}), 200

    @staticmethod
    @SessionController.login_required
    def update_package(work_package_id, **kwargs):
        package = models.WorkPackage.query.filter_by(work_package_id=work_package_id).first()

        if package is None:
            return jsonify({'message': 'package not found'}), 404

        project_id = request.form.get('project_id')
        if project_id is not None:
            package.project_id = int(project_id)

        name = request.form.get('name')
        if name is not None:
            package.name = escape(name)

        description = request.form.get('description')
        if description is not None:
            package.description = escape(description)

        start_timestamp = request.form.get('start_timestamp')
        if start_timestamp is not None:
            package.start_timestamp = escape(start_timestamp)

        end_timestamp = request.form.get('end_timestamp')
        if end_timestamp is not None:
            package.end_timestamp = escape(end_timestamp)

        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def delete_package(work_package_id, **kwargs):
        package = models.WorkPackage.query.filter_by(work_package_id=work_package_id).first()

        if package is None:
            return jsonify({'message': 'package not found'}), 404

        db.session.delete(package)
        db.session.commit()
        return jsonify({'message': 'success'}), 200
