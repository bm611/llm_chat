"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from llm_chat.components.hero import hero
from llm_chat.components import chat
import uuid
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
chat_model = model.start_chat()


class State(rx.State):
    """The app state."""

    input_text: str = ""
    response: str = ""
    is_generating: bool = False
    models: list[str] = []
    history: list[str] = []
    history_roles: list[tuple[str, str]] = []

    character_names = [
        "Zara Moonwhisper",
        "Finnegan Stormrider",
        "Lyra Nightshade",
        "Thorne Blackthorn",
        "Aura Swiftwind",
        "Caspian Frostbeard",
        "Ember Fireheart",
        "Orion Stargazer",
        "Nova Sundancer",
        "Atlas Thunderbolt",
        "Iris Dewdrop",
        "Sage Whisperwind",
        "Raven Shadowweaver",
        "Felix Lightfoot",
        "Luna Moonshadow",
        "Jasper Thornheart",
        "Willow Riverstone",
        "Zephyr Cloudrunner",
        "Aria Skysong",
        "Phoenix Ashborn",
    ]

    async def get_responses(self):
        self.is_generating = True
        self.response = chat_model.send_message(self.input_text).text
        self.history = [hist.parts[0].text for hist in chat_model.history]
        self.history_roles = [
            ("USER" if i % 2 == 0 else "ASSISTANT", msg)
            for i, msg in enumerate(self.history)
        ]
        self.is_generating = False
        self.input_text = ""

    def update_input(self, value: str):
        self.input_text = value

    def set_input_text(self, value: str):
        self.input_text = value

    def create_chat(self):
        new_chat_id = str(uuid.uuid4())
        return rx.redirect(f"/chat/{new_chat_id}")

    def clear_history(self):
        global chat_model
        self.history = []
        chat_model = model.start_chat()
        return rx.redirect("/")

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
