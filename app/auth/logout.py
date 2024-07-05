from flask import flash, redirect, url_for
from flask_login import logout_user
from . import auth_bp


@auth_bp.route("/logout")
def user_logout():
    
    logout_user()
    """
    flash(
        "Successfully logged out, hope to see you soon",
        category="info")
    """
    return redirect(url_for("auth.user_checkpoint"))