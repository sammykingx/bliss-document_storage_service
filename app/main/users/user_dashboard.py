from flask import current_app, render_template
from flask_login import current_user, login_required
from . import user_bp
from app.database  import db_helpers, documents


@user_bp.route("/dashboard")
@login_required
def user_dashboard():
    recent_files  = db_helpers.fetch_recent_files(documents.Documents)
    return render_template(
        "users/dashboard.html",
        user=current_user,
        recent_uploads = recent_files,
    )