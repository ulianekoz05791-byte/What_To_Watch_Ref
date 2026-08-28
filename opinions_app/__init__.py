from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты в конце, чтобы избежать циклических зависимостей
from opinions_app import models, forms, views, error_handlers, cli_commands
