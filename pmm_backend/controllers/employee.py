"""
    Implements the EmployeeController
"""
import json
from flask_restx import fields, marshal
from flask import jsonify, request, escape

from pmm_backend import db
from pmm_backend.models import models
from pmm_backend.controllers.session import SessionController


class EmployeeController:
    """
        Employee Controller Class
    """

    @staticmethod
    @SessionController.login_required
    def list_employees():
        """
        Lists all employees.
        :return:  List of employees in JSON format
        """
        marshaller = {
            'employee_id': fields.Integer,
            'first_name': fields.String,
            'last_name': fields.String,
        }

        all_employees = models.Employee.query.all()
        return json.dumps(marshal(all_employees, marshaller))

    @staticmethod
    @SessionController.login_required
    def add_employee():
        """
        Adds a new employee.
        :return: Status in JSON format
        """
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        if first_name is None:
            return jsonify({'message': 'missing data: first_name'}), 400
        if last_name is None:
            return jsonify({'message': 'missing data: last_name'}), 400

        employee = models.Employee(first_name=escape(first_name), last_name=escape(last_name))

        db.session.add(employee)
        db.session.commit()
        return jsonify({'message': 'success', 'employee_id': employee.employee_id}), 200

    @staticmethod
    @SessionController.login_required
    def update_employee(employee_id):
        """
        Updates an existing employee.
        :param employee_id: ID of the employee
        :return: Status in JSON format
        """
        employee = models.Employee.query.filter_by(employee_id=employee_id).first()

        if employee is None:
            return jsonify('message:' 'employee not found'), 404

        first_name = request.form.get('first_name')
        if first_name is not None:
            employee.first_name = escape(first_name)

        last_name = request.form.get('last_name')
        if last_name is not None:
            employee.last_name = escape(last_name)

        db.session.commit()
        return jsonify({'message': 'success'}), 200

    @staticmethod
    @SessionController.login_required
    def delete_employee(employee_id):
        """
        Deletes an employee.
        :param employee_id: ID of the employee
        :return: Status in JSON format
        """
        employee = models.Employee.query.filter_by(employee_id=employee_id).first()

        if employee is None:
            return jsonify('message:' 'employee not found'), 404

        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'success'}), 200
