from flask import render_template
from flask_login import current_user, login_required
from . import bp


@bp.route("/staff_usage")
@login_required
def staff_documetation():
    return render_template(
        "misc/staff_faq.html",
        user=current_user,
    )