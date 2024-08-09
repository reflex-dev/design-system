"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from components.styles.styles import base_style, base_stylesheets

import components.buttons.feedback.feedback as feedback


class State(rx.State):
    """The app state."""

    form_data: dict

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


   
def index() -> rx.Component:
    return rx.container(
        rx.box(feedback.feedback_button("Test", State)),
    ) 
  

app = rx.App(
    style=base_style,
    stylesheets=base_stylesheets,
    html_lang="en",
    theme=rx.theme(
        id="main-theme",
        appearance="light",
        has_background=True,
        radius="none",
        accent_color="violet",
    ),
)
app.add_page(index)
      