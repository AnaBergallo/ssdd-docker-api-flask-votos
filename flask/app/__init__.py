from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile("local_settings.cfg")
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
api = Api(app)


@app.route('/')
def home():
    return "Esta es la pagina del home. Luego pongo un index.html (?"

from app.logic import *