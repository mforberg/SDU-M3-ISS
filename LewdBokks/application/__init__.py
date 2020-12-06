from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import os

SECRET_KEY = os.urandom(32)

db = SQLAlchemy()
r = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts'

    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        from . import forms
        from . import routes
        from . import baseroutes
        db.create_all()

        app.register_blueprint(routes.database_bp)
        app.register_blueprint(baseroutes.base_bp)

        return app