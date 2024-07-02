from flask import render_template, url_for
from flask_login import current_user, login_required
from . import user_bp


@user_bp.route("/profile")
@login_required
def user_profile():
    return render_template("profile.html", user=current_user)