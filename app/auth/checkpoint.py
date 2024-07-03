from flask import (
    current_app,
    flash,
    redirect,
    request,
    render_template,
    url_for,
)
from werkzeug.security import check_password_hash
from flask_login import login_user
from app.database.users import Users
from app.database import db_helpers
from . import auth_bp, helpers
from app.main import users


@auth_bp.route("/checkpoint", methods=["GET", "POST"])
def user_checkpoint():
    if request.method == "POST":
        user_data = dict(request.form)
        current_app.logger.info(f"form data: {user_data}")
        if not user_data:
            current_app.logger.info("Empty form data")
            flash("kindly enter your credentails to proceed", category="warning")
            return render_template("login.html")

        user_record = db_helpers.fetch_records(
            Users,
            email=user_data.get("email", None)
        )

        if not user_record:
            current_app.logger.info("No user record found")
            flash("Invalid username/password", category="warning")
            return render_template("login.html")

        elif not check_password_hash(
            user_record.password, user_data["password"]
        ):
            current_app.logger.info("Incorrect password")
            flash("Invalid username/password", category="warning")
            return render_template("login.html")

        login_user(user_record)
        flash("succesfully logged in, welcome on board", category="info")
        current_app.logger.info("User logged in")
        
        #user_default_page = helpers.fetch_dashboard_url(user_record.role)
        next_url = request.args.get("next", None)
        alowed_urls = [endpoints.rule for endpoints in current_app.url_map.iter_rules()]
        if next_url not in alowed_urls:
            current_app.logger.info("Before redirect")
            return redirect(url_for("user.user_dashboard"))
        
        return redirect(next_url)
    
    return render_template("login.html")