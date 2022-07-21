import os
from app.models import db
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from .api import game_routes

app = Flask(__name__)
app.config.from_mapping({
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})

app.register_blueprint(game_routes, url_prefix='/game')
db.init_app(app)
Migrate(app, db)

CORS(app)
