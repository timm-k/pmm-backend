"""
    Implements the ProjectController
"""
import json
from flask_restx import fields, marshal
from flask import jsonify, request, escape

from pmm_backend import db
from pmm_backend.models import models
from pmm_backend.controllers.session import SessionController



class ProjectController:
    """
        Project Controller Class
    """

    @staticmethod
    @SessionController.login_required
    def list_projects():
        """
        Lists all projects.
        :return: List of projects in JSON format
        """
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
    @SessionController.login_required
    def add_project():
        """
        Adds a new project.
        :return: Status in JSON format
        """
        name = request.form.get('name')
        description = request.form.get('description')
        start_timestamp = request.form.get('start_timestamp')
        end_timestamp = request.form.get('end_timestamp')

        if name is None:
            return jsonify({'message': 'missing data: name'}), 400
        if description is None:
            return jsonify({'message': 'missing data: description'}), 400
        if start_timestamp is None:
            return jsonify({'message': 'missing data: start_timestamp'}), 400
        if end_timestamp is None:
            return jsonify({'message': 'missing data: end_timestamp'}), 400

        name = escape(name)
        description = escape(description)
        start_timestamp = int(start_timestamp)
        end_timestamp = int(end_timestamp)

        project = models.Project(name=name, description=description,
                                 start_timestamp=start_timestamp, end_timestamp=end_timestamp)

        db.session.add(project)
        db.session.commit()
        return jsonify({'message': 'success', 'project_id': project.project_id}), 200

    @staticmethod
    @SessionController.login_required
    def update_project(project_id):
        """
        Updates an existing project.
        :return: Status in JSON format
        """
        project = models.Project.query.filter_by(project_id=project_id).first()

        if project is None:
            return jsonify({'message': 'project not found'}), 404

        name = request.form.get('name')
        if name is not None:
            project.name = escape(name)

        description = request.form.get('description')
        if description is not None:
            project.description = escape(description)

        start_timestamp = request.form.get('start_timestamp')
        if start_timestamp is not None:
            project.start_timestamp = escape(start_timestamp)

        end_timestamp = request.form.get('end_timestamp')
        if end_timestamp is not None:
            project.end_timestamp = escape(end_timestamp)

        db.session.commit()
        return jsonify('message:' 'success'), 200

    @staticmethod
    @SessionController.login_required
    def delete_project(project_id):
        """
        Deletes a project.
        :return: Status in JSON format
        """
        project = models.Project.query.filter_by(project_id=project_id).first()

        if project is None:
            return jsonify({'message': 'project not found'}), 404

        db.session.delete(project)
        db.session.commit()
        return jsonify('message:' 'success'), 200
