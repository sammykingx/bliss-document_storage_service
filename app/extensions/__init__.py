from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()