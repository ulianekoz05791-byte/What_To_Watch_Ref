from flask import Flask
from flask_migrate import Migrate
from settings import Config
from .extensions import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Импорты после создания app
    from . import views, error_handlers, cli_commands
    
    # Регистрируем blueprint
    app.register_blueprint(views.bp)

    return app
