from connexion import FlaskApp
from flask import render_template
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, event
import geoalchemy2

from config import Config

connex_app = FlaskApp(__name__)

app = connex_app.app
app.config.from_object(Config)
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

ma = Marshmallow(app)
db = SQLAlchemy(app, metadata=metadata)

migrate = Migrate(app, db)


with app.app_context():
    @event.listens_for(db.engine, "connect")
    def load_spatialite(dbapi_conn, connection_record):
        # From https://geoalchemy-2.readthedocs.io/en/latest/spatialite_tutorial.html
        dbapi_conn.enable_load_extension(True)
        dbapi_conn.load_extension('mod_spatialite.dylib')


from app import models


@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Doug'}
    return render_template('home.html', title='Home', user=user)
