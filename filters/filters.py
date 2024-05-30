from aiogram.types import Message

def city_filter(message: Message) -> bool:
    return  '-' in message.text
