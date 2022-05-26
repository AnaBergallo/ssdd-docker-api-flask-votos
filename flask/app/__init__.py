from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("local_settings.cfg")
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)



from app.logic import *

