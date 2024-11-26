import reflex as rx

from ..styles.header import header_style
from ..components.input_box import ChatMessages


def header():
    return (
        rx.flex(
            rx.hstack(
                rx.icon(
                    "eraser",
                    color="gray",
                    stroke_width="2",
                    class_name="cursor-pointer",
                    on_click=ChatMessages.clear(),
                ),
            ),
            style=header_style,
            align="center",
            justify="between",
        ),
    )
