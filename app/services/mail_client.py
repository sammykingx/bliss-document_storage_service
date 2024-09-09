from flask import current_app
from flask_mail import Message
from app.extensions import mail


def send_mail(subject: str, to_email: str, message: str) -> None:
    msg = Message(subject, recipients=[to_email], html=message)
    
    try:
        mail.send(msg)

    except Exception as err:
        current_app.logger.error(err, exc_info=True)