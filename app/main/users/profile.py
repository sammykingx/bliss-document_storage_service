from flask import current_app, jsonify, request, render_template, url_for
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from app.auth import helpers
from . import user_bp


@user_bp.route("/profile")
@login_required
def user_profile():
    return render_template("users/profile.html", user=current_user)


@user_bp.route("/update_profile", methods=["POST"])
@login_required
def update_profile():
    return "<h2>Update Profile</h2>"


@user_bp.route("/update_profile_image")
@login_required
def update_profile_image():
    return "<h2>Update Profile Image</h2>"


@user_bp.route("/update_user_password", methods=["POST"])
@login_required
def update_user_password():
    if request.method == "POST":
        if not check_password_hash(
            current_user.password,
            request.form["current_pwd"]
        ):
            current_app.logger.info(f"user hasedpwd: {current_user.password}")
            return jsonify(
                message="You entered the wrong password",
                category="info",
            )
            
        helpers.update_password(current_user, request.form["new_pwd"])
        return jsonify(
            message="Password Update successful",
            category="success",
        )
        
    return "<h2>Update Profile Password</h2>"