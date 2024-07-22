from flask import render_template
from flask_login import current_user, login_required
from . import bp

@bp.route("/dev_support", methods=["GET", "POST"])
@login_required
def developer_support():
    return render_template(
        "misc/contact.html",
        user=current_user,
    )