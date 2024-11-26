# chatapp.py
import reflex as rx

from .pages import index

style = {"font_family": "Roboto", "background": "#212121", "height": "100%"}

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap",
    ],
    theme=rx.theme(appearance="dark", has_background=True, accent_color="gray"),
    style=style,
)
app.add_page(index, title="Login")
