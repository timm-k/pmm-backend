from pmm_backend import api, settings, db
from pmm_backend.models import models
from flask_restx import fields, marshal

import json


class EmployeeController:

    @staticmethod
    def add_employee(first_name, last_name):
        employee = models.Employee(first_name=first_name, last_name=last_name)

        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def list_employees():
        marshaller = {
            'employee_id': fields.Integer,
            'first_name': fields.String,
            'last_name': fields.String,
        }

        all_employees = models.Employee.query.all()
        return json.dumps(marshal(all_employees, marshaller))

    @staticmethod
    def modify_employee(first_name, last_name):
        employee = models.Employee(first_name=first_name, last_name=last_name)

        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        models.Employee.query.filter_by(employee_id=employee_id).first()
        db.session.commit()