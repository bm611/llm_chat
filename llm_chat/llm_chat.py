"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from llm_chat.components.hero import hero
import uuid


class State(rx.State):
    """The app state."""

    input_text: str = ""

    def update_input(self, value: str):
        self.input_text = value

    def set_input_text(self, value: str):
        self.input_text = value

    def create_chat(self):
        new_chat_id = str(uuid.uuid4())
        return rx.redirect(f"/chat/{new_chat_id}")

    @rx.var
    def get_chat_id(self) -> str:
        return self.router.page.params.get("chat_id", "")


@rx.page("/", title="Chat App")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            hero(State),
        ),
        class_name="w-full",
    )


@rx.page("/chat/[chat_id]", title="Chat Window")
def chat():
    return rx.vstack(
        rx.text(f"Chat ID: {State.get_chat_id}"),
        rx.text(f"Input: {State.input_text}"),
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
