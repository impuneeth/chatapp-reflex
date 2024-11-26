# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "0px 1px 4px -1px rgba(0, 0, 0, 0.46)"


message_style = dict(
    padding_top="10px",
    padding_bottom="10px",
    padding_left="20px",
    padding_right="20px",
    border_radius="24px",
    width="fit-content",
    margin_y="0.5rem",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left="30%",
    background_color=rx.color("gray"),
)
answer_icon_style = dict(
    border_width="0.3px",
    border_radius="30px",
    padding="7px",
    border_color="gray",
)

# Styles for the action bar.
input_style = dict(height="55px", width="55%", margin_left="1rem")
submit_button_style = dict(cursor="pointer", margin="0.5rem", padding="8px")
form_style = dict(
    padding_top="20px",
    background_color="#212121",
    position="sticky",
    bottom="0px",
    padding_bottom="20px",
    z_index="1",
)

header_button = dict(background_color="#FFF", cursor="pointer")

header_style = dict(
    background_color="#212121",
    padding="12px",
    height="64px",
    width="100%",
    position="sticky",
    top="0px",
    z_index="1",
)
header_text = dict(font_size="24px", color="#b4b4b4", font_weight="600")

welcome_font = dict(font_size="30px", font_weight="600")

drawer_style = dict(
    height="1000%",
    width="20%",
    padding="20px",
    background_color="black",
)
