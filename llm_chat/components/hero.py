import reflex as rx
import uuid


class HeroState(rx.State):
    """The app state."""

    def create_chat(self):
        new_chat_id = str(uuid.uuid4())
        return rx.redirect(f"/chat/{new_chat_id}")


def hero() -> rx.Component:
    grid_list = [
        "Brainstorm a tagline for my online store",
        "Why is the sky blue",
        "How to pick ripe watermelon",
        "How much does a cloud weigh",
    ]
    return rx.vstack(
        rx.box(
            rx.heading(
                "Hello, Bharath",
                class_name="mt-20 text-6xl tracking-wide font-regular text-transparent bg-clip-text bg-gradient-to-r from-blue-500 via-pink-500 to-orange-800",
            ),
            rx.text(
                "How can I help you today?",
                class_name="py-2 text-6xl tracking-normal font-semibold text-zinc-700",
            ),
            rx.grid(
                rx.foreach(
                    grid_list,
                    lambda i: rx.card(
                        i, size="4", class_name="text-xl hover:bg-gray-700"
                    ),
                ),
                columns="2",
                spacing="3",
                # width="60%",
                class_name="mt-20",
            ),
        ),
        rx.hstack(
            rx.input(
                placeholder="Enter a prompt here",
                class_name="w-full h-14 px-5 rounded-full text-lg bg-transparent",
            ),
            rx.button(
                rx.icon("arrow-up"),
                class_name="rounded-full bg-gray-700 hover:bg-gray-400",
                size="4",
                on_click=HeroState.create_chat,
            ),
            class_name="w-full flex items-center",
        ),
        class_name="py-10 min-h-screen flex flex-col justify-between items-center",
    )
