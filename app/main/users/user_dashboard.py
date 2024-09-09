from flask import current_app, render_template
from flask_login import current_user, login_required
from . import user_bp
from app.database  import users, db_helpers, documents, notifications


ALL_BRANCHES = (
    "ihama",
    "obakhavbaye",
    "ikeja",
    "ajah",
    "abeokuta",
    "asaba",
)

@user_bp.route("/dashboard")
@login_required
def user_dashboard():
    total_files = len(db_helpers.fetch_records(
            documents.Documents,
            is_thrashed=False,
            is_deleted=False,
        )
    )
    total_clients = len(db_helpers.fetch_records(users.Clients))
    recent_files  = db_helpers.fetch_recent_files(
        documents.Documents,
        is_thrashed=False,
        is_deleted=False,
    )
    recent_activity = db_helpers.fetch_recent_activity(notifications.Notifications)
    
    return render_template(
        "users/dashboard.html",
        user=current_user,
        recent_uploads = recent_files,
        recent_activity = recent_activity,
        branchs=sorted(ALL_BRANCHES),
        total_branch=len(ALL_BRANCHES),
        total_files=total_files,
        total_clients=total_clients,
    )