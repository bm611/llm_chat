"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from llm_chat.components.hero import hero


class State(rx.State):
    """The app state."""


@rx.page("/", title="Chat App")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            hero(),
        ),
        class_name="w-full",
    )


style = {
    "font_family": "ProductSans",
}

app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",
    ],
    style=style,
)
