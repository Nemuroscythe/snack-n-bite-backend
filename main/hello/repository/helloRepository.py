from flask import current_app

from main.hello.models.HelloMessage import HelloMessage
from main.model import db


def get_hello_messages():
    db_response = db.session.execute(db.select(HelloMessage)).all()
    current_app.logger.info(type(db_response))
    return db_response


def get_hello_message(id):
    dbResponse = db.get_or_404(HelloMessage, id)
    return dbResponse


def create_hello_message(hello_message):
    db.session.add(hello_message)
    db.session.commit()
    return None


def update_hello_message(hello_message):
    current_app.logger.debug(hello_message)
    hello_message_db = db.get_or_404(HelloMessage,
                                     hello_message.id)
    hello_message_db.content = hello_message.content
    db.session.commit()
    return None


def delete_hello_message(id):
    hello_message_db = db.get_or_404(HelloMessage, id)
    db.session.delete(hello_message_db)
    db.session.commit()
    return None
