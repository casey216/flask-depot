from flask import Flask, render_template
from .extensions import db, migrate, login_manager
from .config import config
from .blueprints.main.views import main as main_blueprint
from .blueprints.auth.views import auth as auth_blueprint
from .models import *


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login_manager.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html', title = '404'), 404

    return app