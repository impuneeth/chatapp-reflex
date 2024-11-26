import os
from time import sleep
from dotenv import load_dotenv

import reflex as rx
from together import Together

from ..styles.header import (
    message_style,
    question_style,
    answer_icon_style,
)

load_dotenv()


class ChatMessages(rx.State):

    messages: list[dict] = []
    new_chat: bool = True
    role: str = "user"
    show_loading: bool = False

    def clear(self):
        self.messages = []
        self.new_chat = True

    def add_message(self, form_data: dict):
        self.messages.append({"role": "user", "content": form_data["user_input"]})
        self.new_chat = False
        self.show_loading = True
        yield

        client = Together(api_key=str(os.environ["TOGETHER_API_KEY"]))

        response = client.chat.completions.create(
            model="meta-llama/Llama-Vision-Free", stream=False, messages=self.messages
        )
        self.messages.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
        self.show_loading = False


class StreamWelcome(rx.State):
    message: str = ""

    def stream(self):
        self.message = ""
        welcome_message = "How can I help today?"
        for i in welcome_message:
            sleep(0.05)
            self.message = self.message + i
            yield


def messages(chat: dict):
    print(chat)
    return rx.box(
        rx.cond(
            ChatMessages.role == chat["role"],
            rx.flex(
                rx.text(chat["content"], style=question_style),
                direction="row-reverse",
            ),
            rx.flex(
                rx.icon("bot-message-square", style=answer_icon_style, size=40),
                rx.markdown(chat["content"], style=message_style),
            ),
        ),
    )
