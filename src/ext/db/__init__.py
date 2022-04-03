from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)