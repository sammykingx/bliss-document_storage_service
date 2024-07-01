from flask import (
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from itsdangerous.exc import SignatureExpired
from werkzeug.security import generate_password_hash
from app.database.users import Users
from app.database import db_helpers
from app.services import mail_client
from app.extensions import db
from . import auth_bp, helpers


@auth_bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if not token:
        flash(
            message="corrupt URL",
            category="error"
        )
        current_app.logger.info("Bad Token")

        return redirect(url_for("auth.user_checkpoint"))
    
    if request.method == "POST":
        new_pwd = request.form["new_pwd"]
        conf_pwd = request.form["conf_pwd"]
        if new_pwd != conf_pwd:
            flash("passwords doesn't match, check and try again")
            return redirect(url_for("auth.verify_user_email"))

        try:
            user_email = helpers.email_serializer.loads(token, max_age=600)
        
        except SignatureExpired as err:
            flash(
                message="expired email token",
                category="error"
            )
            
            return redirect(url_for("auth.user_checkpoint"))
        
        user_record = db_helpers.fetch_records(Users, email=user_email)
        user_record.password = generate_password_hash(new_pwd)
        db.session.add(user_record)
        db.session.commit()
        db.session.refresh(user_record)
        current_app.logger.info(f"User password changed: {new_pwd}")
     
    return redirect(url_for("auth.user_checkpoint"))


@auth_bp.route("/request_email_token", methods=["GET", "POST"])
def verify_user_email():
    
    if request.method == "POST":
        user_email = request.form["email"]
        #user_record = db_helpers.fetch_records(
        #    Users,
        #    email=user_email,
        #)
        
        #if not user_record:
        #    flash(
        #        message="Enter a registered email to get reset token",
        #        category="info",
        #    )
            
        #    return redirect(url_for("auth.user_checkpoint"))
        
        token = helpers.email_serializer.dumps(user_email)
        reset_url = url_for("auth.reset_password", token=token)
        
        email_msg = render_template(
            "email/reset_password.html",
            reset_url=reset_url)

        current_app.logger.info(f">>> {reset_url}")
        mail_client.send_mail(
            subject="BLL Password Reset",
            to_email=user_email,
            message=email_msg,
        )
        flash(
            message="Kindly check your email to proceed",
            category="info",
        )
        
        
    return render_template("request_password_token.html")