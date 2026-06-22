from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from database import get_session
from passlib.context import CryptContext
from fastapi_mail import ConnectionConfig, FastMail, MessageType, MessageSchema


SessionDep = Annotated[Session, Depends(get_session)]

pwd_context = CryptContext(schemes=["sha256_crypt"])


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


conf = ConnectionConfig(
    MAIL_USERNAME ="aydinfakhri9@gmail.com",
    MAIL_PASSWORD = "jltsmnefrqcenzmo",
    MAIL_FROM = "aydinfakhri9@gmail.com",
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

html = """ <b> Thanks for your registration :) </b> """
fm = FastMail(conf)

async def send_email(email):
    message = MessageSchema(subject="Registration", recipients=[email], body=html, subtype=MessageType.html)
    await fm.send_message(message)
    return True