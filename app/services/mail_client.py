from flask import current_app
from flask_mail import Message
#from app.core import logger
from app.extensions import mail


def send_mail(subject: str, to_email: str, message: str) -> None:
    msg = Message(subject, recipients=[to_email], html=message)
    
    try:
        current_app.logger.info("About sending email")
        mail.send(msg)
        current_app.logger.info("Email sent successfully")

    except Exception as err:
        current_app.logger.error(err, exc_info=True)