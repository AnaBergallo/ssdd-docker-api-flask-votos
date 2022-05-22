from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("local_settings.cfg")
    app.url_map.strict_slashes = False
    db = SQLAlchemy(app)
    api = Api(app)
    migrate = Migrate(app, db)
    return {'app': app, 'api':api, 'db': db}

obj = create_app()
app,api,db = obj['app'], obj['api'], obj['db']

from app.logic import *

