import reflex as rx

from ..styles.header import drawer_style
from ..components.message_box import ChatMessages


class DrawerState(rx.State):
    is_open: bool = True

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open


def drawer_content():
    return rx.drawer.content(
        rx.drawer.close(
            rx.flex(
                rx.icon(
                    "panels-top-left",
                    color="gray",
                    stroke_width="2",
                    class_name="cursor-pointer",
                ),
                rx.icon(
                    "eraser",
                    color="gray",
                    stroke_width="2",
                    class_name="cursor-pointer",
                    on_click=ChatMessages.clear(),
                ),
                direction="row",
                justify="between",
                style=drawer_style,
            ),
        )
    )
