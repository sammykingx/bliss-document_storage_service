from flask import (
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import generate_password_hash
from app.database.users import Users
from app.database import db_helpers
from app.services import mail_client
from app.extensions import db
from . import auth_bp, helpers


@auth_bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        form_data = request.form
        if helpers.is_email_token_present(form_data["token"]):
            return jsonify(
                message="Invalid token, try again",
                category="error",
                redirect_url=url_for("auth.user_checkpoint"),
            ), 400

        token_data = helpers.get_token_data(form_data["token"])
        if not token_data["valid"]:
            return jsonify(
                message=token_data["message"],
                category="error",
            ), 400
            
        user_record = db_helpers.fetch_records(Users, email=token_data["data"])
        helpers.update_password(user_record, form_data["password"])
    
        current_app.logger.info(f"User password changed: {user_record.email}")
        return jsonify(
            message="Password reset successful",
            category="success",
            redirect_url=url_for("auth.user_checkpoint"),
        )
    
    return render_template("auth/reset_password.html")


@auth_bp.route("/request_email_token", methods=["GET", "POST"])
def verify_user_email():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_record = db_helpers.fetch_records(
            Users,
            email=user_email,
        )
        
        if not user_record:
            return jsonify(
                message="Enter a registered email to get reset token",
                category="warning",
            ), 400
        
        token = helpers.email_serializer.dumps(user_email)
        reset_endpoint = "http://localhost:5000{}".format(url_for("auth.reset_password", token=token))
        
        email_msg = render_template(
            "email/reset_email_token.html",
            reset_url=reset_endpoint)

        current_app.logger.info(f">>> {reset_endpoint}")

        mail_client.send_mail(
            subject="BLL Password Reset",
            to_email=user_email,
            message=email_msg,
        )
        
        return jsonify(
            message="Kindly check your email to proceed",
            category="info",
        )       

    return render_template("auth/request_password_token.html")