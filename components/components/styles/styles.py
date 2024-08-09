from ..styles.colors import c_color
import reflex as rx

base_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700;800&display=swap",
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700;800&text=%E2%86%97&display=swap",  # Include the north-east arrow unicode
    "style.css",
    "custom_colors.css",
]

base_style = {
    "font-family": "Instrument Sans",
    "background": c_color("slate", 2),
    "transition": "filter 0.1s ease-out",
    # Remove the underline from the links
    rx.link: {
        "text_decoration": "none !important",
    },
}
