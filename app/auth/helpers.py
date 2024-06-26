from flask import Flask, url_for
from itsdangerous import URLSafeTimedSerializer
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