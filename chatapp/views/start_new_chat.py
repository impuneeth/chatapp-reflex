import reflex as rx
from ..components import header, input_box, messages, ChatMessages, StreamWelcome
from ..styles.header import welcome_font, answer_icon_style


def new_chat():
    return rx.box(
        header(),
        rx.cond(
            ChatMessages.new_chat,
            rx.flex(
                rx.text(StreamWelcome.message, style=welcome_font),
                rx.icon("dot", stroke_width=20),
                min_height="calc(100vh - 64px - 121px)",
                align="center",
                justify="center",
                direction="row",
                spacing="2",
            ),
            rx.container(
                rx.scroll_area(
                    rx.foreach(
                        ChatMessages.messages,
                        messages,
                    ),
                    type="hover",
                ),
                rx.cond(
                    ChatMessages.show_loading,
                    rx.flex(
                        rx.icon("bot-message-square", style=answer_icon_style, size=40),
                        rx.skeleton(
                            rx.box(width="50%", height="30px"),
                            loading=ChatMessages.show_loading,
                        ),
                        align="center",
                        spacing="2",
                        margin_y="0.6rem",
                    ),
                ),
                min_height="calc(100vh - 64px - 121px)",
                z_index="0",
            ),
        ),
        input_box(),
        stack_children_full_width=True,
    )
