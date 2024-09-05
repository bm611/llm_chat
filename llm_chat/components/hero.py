import reflex as rx
import random


def hero(state) -> rx.Component:
    grid_list = [
        "Brainstorm a tagline for my online store",
        "Why is the sky blue",
        "How to pick ripe watermelon",
        "How much does a cloud weigh",
    ]
    # character = random.choice(state.character_names)
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.heading(
                    "Hello, Bharath",
                    class_name="text-6xl tracking-wide font-regular text-transparent bg-clip-text bg-gradient-to-r from-blue-500 via-pink-500 to-orange-800",
                ),
                rx.icon(
                    "sparkles",
                    size=40,
                    color="var(--indigo-10)",
                ),
                class_name="mt-20 flex items-center",
            ),
            rx.text(
                "How can I help you today?",
                class_name="py-2 text-6xl tracking-normal font-semibold text-zinc-700",
            ),
            rx.grid(
                rx.foreach(
                    grid_list,
                    lambda i: rx.card(
                        i,
                        size="4",
                        class_name="text-2xl cursor-pointer",
                        style=rx.Style(
                            {
                                "border-width": "2px",
                                "border-style": "solid",
                                "&:hover": {
                                    "border-color": "violet",
                                    "border-width": "4px",
                                    "border-style": "solid",
                                },
                            }
                        ),
                        on_click=lambda: state.set_input_text(i),
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
                on_change=state.update_input,
                value=state.input_text,
            ),
            rx.button(
                rx.icon("arrow-up"),
                class_name="rounded-full bg-gray-700 hover:bg-gray-400",
                size="4",
                on_click=state.create_chat,
                type="submit",
            ),
            class_name="w-full flex items-center",
        ),
        class_name="py-10 min-h-screen flex flex-col justify-between items-center",
        # on_mount=state.get_models,
    )
