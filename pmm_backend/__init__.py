from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pmm_backend import settings

api = Flask(__name__)
api.config.from_pyfile('settings.py')

db = SQLAlchemy(api)

from pmm_backend.controllers import user