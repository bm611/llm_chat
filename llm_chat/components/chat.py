import reflex as rx


# TODO: use chat.history to loop through "user" and "model" responses
# create vstack of hstack of {USER ICON} : {USER INPUT} followed by {MODEL ICON} : {MODEL OUTPUT}
# keep "CLEAR CHAT" and "INPUT FIELD" visible at all times
def display(val):
    return rx.vstack(
        rx.text(val[0], class_name="text-gray-400"),
        rx.markdown(val[1], class_name="text-xl"),
        rx.spacer(),
    )


def chat_window(state) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.foreach(state.history_roles, display),
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
                    class_name="rounded-full bg-gray-700 hover:bg-red-600",
                    size="4",
                    on_click=state.clear_history,
                    type="submit",
                ),
                class_name="w-full flex items-center py-10",
            ),
            class_name="min-h-screen",
        ),
        class_name="max-w-screen-md mx-auto p-10",
    )
