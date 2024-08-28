"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from llm_chat.components.hero import hero


class State(rx.State):
    """The app state."""

    @rx.var
    def get_chat_id(self) -> str:
        return self.router.page.params.get("chat_id", "")


@rx.page("/", title="Chat App")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            hero(),
        ),
        class_name="w-full",
    )


@rx.page("/chat/[chat_id]", title="Chat Window")
def chat():
    return rx.text(f"Chat ID: {State.get_chat_id}")


style = {
    "font_family": "ProductSans",
}

app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",
    ],
    style=style,
)
