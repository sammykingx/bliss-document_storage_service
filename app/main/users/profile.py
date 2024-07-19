from flask import render_template, url_for
from flask_login import current_user, login_required
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


@user_bp.route("/update_profile_password")
@login_required
def user_profile_password():
    return "<h2>Update Profile Password</h2>"