import os
from pathlib import Path
from dotenv import load_dotenv
#from sqlalchemy import QueuePool


load_dotenv()

BASE_DIR = Path(__file__).parent
UPLOAD_DIR = os.path.join(BASE_DIR.parent, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

class DevelopmentConfig:

    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")
    #SQLALCHEMY_ENGINE_OPTIONS = {
    #    "pool": QueuePool,
    #    "pool_pre_ping": True,
    #    "pool_size": 100,
    #    "pool_recycle": 3600,
    #}

    MAIL_SERVER = os.getenv("SMTP_HOST")
    MAIL_PORT = int(os.getenv("SMTP_PORT"))
    MAIL_USE_SSL = bool(os.getenv("USE_SSL"))
    MAIL_USERNAME = os.getenv("SMTP_MAIL")
    MAIL_PASSWORD = os.getenv("SMTP_PWD")
    MAIL_DEFAULT_SENDER = os.getenv("SMTP_MAIL")
    
    # File uploads Config
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    UPLOAD_FOLDER = UPLOAD_DIR
    ALLOWED_FILE_TYPES = (
        "application/msword",
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )