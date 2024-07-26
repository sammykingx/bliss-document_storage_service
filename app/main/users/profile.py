from flask import current_app, jsonify, request, render_template, url_for
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from app.auth import helpers
from app.database import db_helpers
from app.database.users import Users, SocialMedia
from . import user_bp


@user_bp.route("/profile")
@login_required
def user_profile():
    return render_template("users/profile.html", user=current_user)


@user_bp.route("/update_profile", methods=["POST"])
@login_required
def update_profile():
    """Updates user profile information"""

    payload = dict(request.form)
    user_about = payload.pop("about")
    db_helpers.update_record(Users, current_user.email, about=user_about)
    payload.update({"email": current_user.email})
    if current_user.social_media:
        db_helpers.update_record(SocialMedia, current_user.email, **payload)

    else:
        db_helpers.save_record(SocialMedia, **payload)

    return jsonify(
        message="Profile Update successful",
        category="success",
    )


@user_bp.route("/update_profile_image")
@login_required
def update_profile_image():
    return "<h2>Update Profile Image</h2>"


@user_bp.route("/update_user_password", methods=["POST"])
@login_required
def update_user_password():
    if not check_password_hash(
        current_user.password,
        request.form["current_pwd"]
    ):
        return jsonify(
            message="You entered the wrong password",
            category="info",
        )
            
    helpers.update_password(current_user, request.form["new_pwd"])
        
    return jsonify(
        message="Password Update successful",
        category="success",
    )