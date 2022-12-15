from flask import current_app

from main.hello.models.HelloMessage import HelloMessage
from main.hello.service.dto.HelloMessageDTO import HelloMessageDTO
from main.hello.service.dto.HelloMessagesDTO import HelloMessagesDTO


def convert_hello_message_to_dto(hello_message):
    return HelloMessageDTO(hello_message.content)


def convert_json_to_hello_message(hello_message_json, id=None):
    current_app.logger.debug(hello_message_json)
    content = hello_message_json["content"]
    hello_message = HelloMessage(content, id)
    return hello_message


def convert_hello_message_row_to_dto(hello_message):
    hello_message = hello_message[0]  # Row est une classe de SQLAlchemy qui fonctionne comme un tuple
    return HelloMessagesDTO(hello_message.id, hello_message.content)


def convert_hello_message_list_to_dto(hello_messages):
    hello_messages_dto = map(convert_hello_message_row_to_dto, hello_messages)
    return list(hello_messages_dto)
