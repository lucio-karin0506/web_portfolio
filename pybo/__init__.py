from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # config.py 파일에 작성한 항목 app.config 환경 변수로 불러옴.
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app