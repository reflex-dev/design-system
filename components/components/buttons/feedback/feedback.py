import reflex as rx
from . import styles as st

def emoji_item(emoji: str, value: str) -> rx.Component:
    return rx.radio_cards.item(
        rx.icon(emoji, color=st.fill_secondary_color, z_index=1),
        value=value,
        style=st.emoji_card_style,
    )

def emojis_card() -> rx.Component:
    return rx.hstack(
        rx.radio_cards.root(
            emoji_item("frown", "😢"),
            emoji_item("meh", "😐"),
            emoji_item("smile", "😀"),
            default_value="",
            columns="3",
            size="1",
            variant="classic",
            gap="16px",
            name="score",
        ),
        align="center",
        justify="start",
        width="100%",
    )

def feedback_content(name, FeedbackState) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Send feedback", style=st.header_text_style),
            rx.form(
                rx.vstack(
                    rx.el.textarea(
                        name="feedback",
                        placeholder=f"What do you think of {name}?",
                        type="text",
                        max_length=500,
                        enter_key_submit=True,
                        resize="vertical",
                        style=st.text_area_style,
                        required=True,
                    ),
                    emojis_card(),
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="Contact email (optional)",
                        style=st.input_style,
                        max_length=100,
                    ),
                    rx.hstack(
                        rx.popover.close(
                            rx.el.button(
                                rx.box(
                                    style=st.rectangle_style,
                                ),
                                "Send",
                                style=st.send_button_style,
                                type="submit",
                            ),
                        ),
                        rx.popover.close(
                            rx.el.button("Cancel", style=st.cancel_button_style)
                        ),
                        align="center",
                        justify="between",
                        width="100%",
                    ),
                    gap="16px",
                    align="start",
                    width="100%",
                ),
                reset_on_submit=True,
                on_submit=FeedbackState.handle_submit,
            ),
            gap="16px",
            align="start",
            width="100%",
        ),
        style=st.feedback_box_style,
    )
 

def feedback_button(name, state) -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.hstack(
                rx.icon("message-square-more", color=st.fill_secondary_color),
                rx.text(
                    "Feedback",
                    style=st.menu_item_text,
                    display=["none", "none", "none", "flex"],
                ),
                style=st.items_style,
            ),
        ),
        rx.popover.content(
            feedback_content(name, state),
            bg="transparent",
            box_shadow="None",
            overflow="visible",
            padding="0px",
            border="none",
            align="center",
        ),
        on_open_change=lambda _: rx.call_script(
            "document.getElementById('main-theme').classList.toggle('blurred-bg')"
        ),
    )
