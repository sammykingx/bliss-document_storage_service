from flask import Blueprint, render_template
from flask_login import current_user, login_required


bp = Blueprint("documents", __name__)

@bp.route("/all_documents")
@login_required
def fetch_all_docs():
    return render_template("documents.html")


@bp.route("/upload_documents")
@login_required
def upload_doc():
    return render_template("uploads.html")


@bp.route("/download_documents")
@login_required
def download_document():
    return "<h2>Download Document</h2>"


@bp.route("/delete_documents")
@login_required
def delete_document():
    return "<h2>Delete Document</h2>"