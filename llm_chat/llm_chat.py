"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from llm_chat.components.hero import hero
from llm_chat.components import nav
from llm_chat.components import chat
from llm_chat.api import llm
import uuid
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


class State(rx.State):
    """The app state."""

    input_text: str = ""
    models: list[str] = []
    selected_model: str = ""
    response: str = ""
    is_generating: bool = False

    def get_models(self):
        self.models = llm.get_model_list(genai)

    # def get_responses(self):
    #     self.response = llm.get_response(model, self.input_text)
    #     self.input_text = ""

    async def get_responses(self):
        self.is_generating = True
        self.response = ""
        async for chunk in llm.get_response(model, self.input_text):
            self.response += chunk
            yield
        self.is_generating = False
        self.input_text = ""

    def set_selected_model(self, model: str):
        self.selected_model = model

    def update_input(self, value: str):
        self.input_text = value

    def set_input_text(self, value: str):
        self.input_text = value

    def create_chat(self):
        new_chat_id = str(uuid.uuid4())
        # self.response = llm.get_response(model, self.input_text)
        # self.input_text = ""
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


@rx.page("/chat/[chat_id]", title="Chat Window", on_load=State.get_responses)
def chat_page():
    return chat.chat_window(State)


style = {
    "font_family": "ProductSans",
}

app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",
    ],
    style=style,
)
