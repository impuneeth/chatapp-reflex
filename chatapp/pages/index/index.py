import reflex as rx
from typing import List

from chatapp.views import new_chat
from chatapp.components.message_box import StreamWelcome


@rx.page("/", "AI Chatbot", on_load=StreamWelcome.stream())
def index():
    return new_chat()
