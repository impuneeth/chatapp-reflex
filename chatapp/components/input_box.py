import os
from dotenv import load_dotenv

import reflex as rx

from ..styles.header import input_style, submit_button_style, form_style
from .message_box import ChatMessages

load_dotenv()


def input_box():
    return rx.form(
        rx.flex(
            rx.input(
                rx.button(
                    rx.icon("arrow-up"),
                    size="3",
                    variant="classic",
                    type="submit",
                    style=submit_button_style,
                    radius="full",
                    disabled=ChatMessages.show_loading,
                ),
                placeholder="Enter your question here",
                name="user_input",
                required=True,
                variant="soft",
                color_scheme="gray",
                radius="full",
                style=input_style,
            ),
            align="center",
            justify="center",
        ),
        rx.text(
            "Everyone makes mistakes! So..just verify the answers once.",
            size="1",
            margin_top="0.5rem",
        ),
        text_align="center",
        style=form_style,
        on_submit=ChatMessages.add_message(),
        reset_on_submit=True,
    )
