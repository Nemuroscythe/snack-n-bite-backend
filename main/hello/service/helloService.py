from main.hello.repository import helloRepository
from main.hello.service import helloMapper


def get_hello_messages():
    hello_message = helloRepository.get_hello_messages()
    return helloMapper.convert_hello_message_list_to_dto(hello_message)


def get_hello_message(id):
    hello_message = helloRepository.get_hello_message(id)
    return helloMapper.convert_hello_message_to_dto(hello_message)


def create_hello_message(hello_message_json):
    hello_message = helloMapper.convert_json_to_hello_message(hello_message_json)
    helloRepository.create_hello_message(hello_message)
    return helloMapper.convert_hello_message_to_dto(hello_message)


def update_hello_message(id, hello_message_json):
    hello_message = helloMapper.convert_json_to_hello_message(hello_message_json, id)
    helloRepository.update_hello_message(hello_message)
    return None


def delete_hello_message(id):
    helloRepository.delete_hello_message(id)
    return None
