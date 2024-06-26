from flask import Flask
from config.dev_config import DevelopmentConfig
from app.extensions import db, mail
from app.extensions.login_system import login_manager
from app.database import seed_db
from . import auth


def create_app(config_class: object = DevelopmentConfig) -> Flask:
    "application factory"
    
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    # initialize extensions
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    
    
    
    # creating db tables
    with app.app_context():
        db.create_all()
        seed_db.run()
    
    # register blueprints
    app.register_blueprint(auth.auth_bp)
    
    
    return app