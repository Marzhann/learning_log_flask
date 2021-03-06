""" Initialize Flask application """
from flask import Flask

from .extentions import db, migrate, login, bootstrap
#from learning_logs.views import ll_bp
#from users.views import users_bp


def create_app(config_file='config.py'):
    """ Create Flask app. """
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
   
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from .learning_logs.views import ll_bp
    from .users.views import users_bp

    app.register_blueprint(ll_bp)
    app.register_blueprint(users_bp)

    return app             

