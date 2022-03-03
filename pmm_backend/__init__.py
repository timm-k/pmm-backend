from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from pmm_backend import settings

api = Flask(__name__)
api.config.from_pyfile('settings.py')
CORS(api)

db = SQLAlchemy(api)

from pmm_backend.controllers.routes import RoutesController

