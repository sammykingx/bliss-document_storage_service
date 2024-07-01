from flask import render_template
from flask_login import current_user, login_required
from . import user_bp


@user_bp.route("/dashboard")
@login_required
def user_dashboard():
    
    return render_template("layout.html", user=current_user)