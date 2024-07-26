from flask import current_app, jsonify, request, render_template, send_from_directory, send_file
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from app.auth import helpers
from app.database import db_helpers
from app.database.users import Users, SocialMedia
from . import user_bp
import os


@user_bp.route("/profile")
@login_required
def user_profile():
    """Renders user profile page"""

    return render_template(
        "users/profile.html",
        user=current_user,
    )


@user_bp.route("/profile_image/<img_name>")
def profile_image(img_name):
    """Serves user profile image"""

    profile_img = os.path.join(
        current_app.config["UPLOAD_PROFILE_FOLDER"],
        img_name
    )

    return send_file(profile_img)

@user_bp.route("/update_profile", methods=["PUT"])
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


@user_bp.route("/update_profile_image", methods=["PATCH"])
@login_required
def update_profile_image():
    """Updates user profile image"""

    prf_img = request.files["profile_image"]
    prf_img_name = secure_filename(prf_img.filename)
    
    if current_user.profile_img:
        os.remove(
            os.path.join(
                current_app.config["UPLOAD_PROFILE_FOLDER"],
                current_user.profile_img,
            )
        )

    db_helpers.update_record(
        Users,
        current_user.email,
        profile_img=prf_img_name,
    )
    
    prf_img.save(
        os.path.join(
            current_app.config["UPLOAD_PROFILE_FOLDER"],
            prf_img_name
        ),
        buffer_size=250*1024,
    )
    
    
    return jsonify(
        message="Profile Image Update successful",
        category="success",
    )


@user_bp.route("/delete_profile_image", methods=["DELETE"])
@login_required
def delete_profile_image():
    """Deletes user profile image"""

    if not current_user.profile_img:
        return jsonify(
            message="You've Not Uploaded a Profile Image",
            category="info",
        )
    
    os.remove(
        os.path.join(
            current_app.config["UPLOAD_PROFILE_FOLDER"],
            current_user.profile_img,
        )
    )

    db_helpers.update_record(
        Users,
        current_user.email,
        profile_img=None,
    )

    return jsonify(
        message="Profile Image Deleted successful",
        category="success",
    )

@user_bp.route("/update_user_password", methods=["PATCH"])
@login_required
def update_user_password():
    """Updates user password"""

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