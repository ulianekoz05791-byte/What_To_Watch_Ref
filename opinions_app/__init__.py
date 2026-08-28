from opinions_app import models, forms, views, error_handlers, cli_commands
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config
from .extensions import db


migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# Импорты в конце, чтобы избежать циклических зависимостей
