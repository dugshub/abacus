from flask import render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import connexion
from config import Config, basedir

connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("swagger.yml")
app = connex_app.app

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
#
@app.route("/")
def home():
    return render_template("home.html")
