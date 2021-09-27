from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import project.config as config

# export FLASK_APP=__init__ 
# export FLASK_ENV=development

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
