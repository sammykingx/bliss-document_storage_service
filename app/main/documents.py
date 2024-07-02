from flask import Blueprint, render_template
from flask_login import current_user, login_required


bp = Blueprint("documents", __name__)

@bp.route("/upload")
@login_required
def upload_doc():
    return render_template("uploads.html")


@bp.route("/all_docs")
@login_required
def fetch_all_docs():
    return render_template("documents.html")