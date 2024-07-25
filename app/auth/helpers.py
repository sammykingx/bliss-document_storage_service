from flask import Flask, url_for
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import SignatureExpired
from werkzeug.security import generate_password_hash
from sqlalchemy import Table
from app.extensions import db
from dotenv import load_dotenv
import os


load_dotenv()
email_serializer = URLSafeTimedSerializer(
        os.getenv("SERIALIZER_KEY"), salt="email_verification"
)


def is_safe_url(app_instance: Flask, endpoint: str, is_https: bool = True) -> bool:
    """checks a url to prevent open redirects"""

    allowed_urls = [endpoints.rule for endpoints in app_instance.url_map.iter_rules()]
    if endpoint not in allowed_urls:
        return False

    if not is_https:
        return False

    return True


def fetch_dashboard_url(user_role) -> str:
    """Returns the authenticated user dashbaord url"""

    if user_role == "user":
        return url_for("users.render_dashboard")

    elif user_role == "admin":
        return url_for("admin.render_dashboard")

    return url_for("index")


def is_email_token_present(token: str | None) -> bool:
    """checks if email token is present"""

    # if token is None, return False
    if token is None:
        return False

    return True


def get_token_data(token: str) -> dict[str, str]:
    """returns the data in the token"""

    try:
        data = email_serializer.loads(token, max_age=300)
        return {"valid": True, "data": data}

    except SignatureExpired:
        return {
            "valid": False,
            "message": "expired email token",
        }
        
        
def update_password(user_record: Table, password: str) -> None:
    "Updates user password"
    
    user_record.password = generate_password_hash(password)
        
    db.session.add(user_record)
    db.session.commit()
    db.session.refresh(user_record)