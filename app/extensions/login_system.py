from flask_login import LoginManager
from app.database.users import Users


login_manager = LoginManager()
login_manager.login_view = "auth.user_checkpoint"
login_manager.login_message = "User authentication is required for this page"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(email):
    """get the authenticated user from session"""

    return Users.query.filter_by(email=email).first()