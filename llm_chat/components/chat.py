import reflex as rx


def display(val):
    return rx.vstack(
        rx.heading(
            val[0],
            class_name="text-2xl font-regular text-transparent bg-clip-text bg-gradient-to-r from-blue-500 via-pink-500 to-orange-800",
        ),
        rx.markdown(val[1], class_name="text-xl"),
        class_name="mt-10",
    )


def chat_window(state) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.foreach(state.history_roles, display),
                    spacing="2",
                    align_items="stretch",
                    # width="80%",
                ),
                height="calc(100vh - 100px)",
                overflow_y="auto",
                padding_bottom="30px",
            ),
            rx.spacer(),
            rx.hstack(
                rx.input(
                    placeholder="Ask a follow up",
                    class_name="w-full h-14 px-5 rounded-full text-lg bg-transparent",
                    on_change=state.update_input,
                    value=state.input_text,
                ),
                rx.button(
                    rx.icon("arrow-up"),
                    class_name="rounded-full bg-gray-700 hover:bg-gray-400",
                    size="4",
                    on_click=state.get_responses,
                    type="submit",
                ),
                rx.button(
                    rx.icon("eraser"),
                    class_name="rounded-full bg-red-600",
                    size="4",
                    on_click=state.clear_history,
                    type="submit",
                ),
                class_name="w-full flex items-center py-10 fixed bottom-0 left-0 right-0 mx-auto max-w-screen-lg",
            ),
            height="100vh",
            width="100%",
        ),
        class_name="max-w-screen-lg mx-auto",
    )
