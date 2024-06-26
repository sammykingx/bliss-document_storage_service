from flask import flash, redirect, render_template, request, url_for
from itsdangerous.exc import SignatureExpired
from app.database.users import Users
from app.database import db_helpers
from . import auth_bp, helpers


@auth_bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if not token:
        flash(
            message="corrupt URL",
            category="error"
        )
        return redirect(url_for("user_checkpoint"))
    
    if request.method == "POST":
        try:
            user_email = helpers.email_serializer.loads(token, max_age=600)
        
        except SignatureExpired as err:
            flash(
                message="expired email token",
                category="error"
            )
            return redirect(url_for("user_checkpoint"))
        
        # update password
     
    return "reset_password.html"


@auth_bp.route("/request_email_token", methods=["GET", "POST"])
def verify_user_email():
    
    if request.method == "POST":
        user_record = db_helpers.fetch_records(Users, email=request.form["email"])
        if not user_record:
            flash(
                message="Enter a registered email to get reset token",
                category="info",
            )
            return redirect(url_for("user_checkpoint"))
            
        # send password reset email
        
    return render_template("request_password_token.html")