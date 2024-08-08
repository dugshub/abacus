from app import db, ma, app
from app.models import Dimension, dimensions_schema


def read_all():
    with app.app_context():
        dimensions = db.session.query(Dimension).all()
        return dimensions_schema.dump(dimensions)