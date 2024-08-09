from ...styles.colors import c_color
from ...styles.fonts import base, base_semibold

bg_color = c_color("slate", 4)
fill_secondary_color = c_color("slate", 9)
menu_item_text_color = c_color("slate", 9)
menu_item_bg = c_color("slate", 2)
stroke_color = c_color("slate", 5)


menu_item_text = {
    "font-family": "Instrument Sans",
    "font-style": "normal",
    "font-weight": "500",
    "font-size": "16px",
    "line-height": "24px",
    "letter-spacing": "-0.015em",
    "color": menu_item_text_color,
}

common_item_style = {
    "align-items": "center",
    "width": "auto",
    "gap": "8px",
    "justify-content": "start",
    "cursor": "pointer",
    "border-radius": "12px",
    "_hover": {
        "background-color": bg_color,
    },
    "transition": "background-color 0.05s ease-out",
    "overflow": "hidden",
}

items_style = {
    **common_item_style,
    "padding": "4px 8px",
}

# Feedback

fill_secondary_color = c_color("slate", 9)
bg_color = c_color("slate", 4)
box_shadow = "0px 24px 12px rgba(28, 32, 36, 0.02), 0px 8px 8px rgba(28, 32, 36, 0.02), 0px 2px 6px rgba(28, 32, 36, 0.02)"

input_style = {
    "color": c_color("slate", 11),
    **base,
    "background-color": c_color("white", 1),
    "border": f"1px solid {c_color('slate', 4)}",
    "width": "100%",
    "height": "100%",
    "padding": "8px 12px",
    "border-radius": "12px",
    "box-sizing": "border-box",
    "outline": "none",
    "&::placeholder": {"color": c_color("slate", 9)},
}

text_area_style = {
    "color": c_color("slate", 11),
    **base,
    "background-color": c_color("white", 1),
    "border": f"1px solid {c_color('slate', 4)}",
    "width": "100%",
    "height": "100%",
    "padding": "8px 12px",
    "border-radius": "12px",
    "max-height": "300px",
    "min-height": "72px",
    "field-sizing": "content",
    "box-sizing": "border-box",
    "outline": "none",
    "overflow-y": "auto",
    "&::placeholder": {"color": c_color("slate", 9)},
}

common_style = {
    "width": "32px",
    "height": "32px",
    "border-radius": "10px",
    "cursor": "pointer",
    "_hover": {
        "background-color": bg_color,
    },
    "color": fill_secondary_color,
    "transition": "all 0.05s ease-out",
}

stroke_color = c_color("slate", 5)

feedback_box_style = {
    "box-sizing": "border-box",
    "padding": "16px",
    "width": "352px",
    "height": "auto",
    "max-height": "564px",
    "background-color": c_color("white", 1),
    # "border": f"1px solid {stroke_color}",
    "box-shadow": box_shadow,
    "border-radius": "26px",
}

header_text_style = {
    "font-style": "normal",
    "font-weight": "500",
    "font-size": "20px",
    "line-height": "28px",
    "letter-spacing": "-0.015em",
    "color": c_color("slate", 11),
}

content_text_style = {
    **base,
    "color": c_color("slate", 9),
}

button_common_style = {
    **base_semibold,
    "display": "flex",
    "align-items": "center",
    "justify-content": "center",
    "padding": "8px 14px",
    "width": "auto",
    "height": "36px",
    "border-radius": "10px",
}

bg_color = (
    f"linear-gradient(180deg, {c_color('violet', 9)} 0%, {c_color('violet', 10)} 100%)"
)
hover_bg = c_color("violet", 9)

send_button_style = {
    **button_common_style,
    "position": "relative",
    "background": bg_color,
    "color": "#FFFFFF",
    "cursor": "pointer",
    "_hover": {
        "background": hover_bg,
    },
}

rectangle_style = {
    "box-sizing": "border-box",
    "position": "absolute",
    "left": "1px",
    "right": "1px",
    "top": "1px",
    "bottom": "1px",
    "border-top": "1px solid rgba(255, 255, 255, 0.22)",
    "border-radius": "11px",
    "z-index": 1,
}

cancel_button_style = {
    **button_common_style,
    "background": c_color("slate", 4),
    "color": c_color("slate", 9),
    "_hover": {
        "background": c_color("slate", 5),
    },
}

# Emojis

emoji_card_style = {
    "border-radius": "12px",
    "cursor": "pointer",
    "border": f"1px solid {c_color('slate', 4)}",
    "--base-card-border-width": "0px",
    "outline": "none",
    "--radio-cards-item-background-color": c_color("white", 1),
    "box-sizing": "border-box",
    "box-shadow": "none",
    "transition": "background-color 0.05s ease-out",
    "_hover::before": {
        "background-color": c_color("slate", 4),
    },
    "::before": {
        "border-radius": "12px",
        "outline": "none",
        "background-color": c_color("white", 1),
    },
    "&[data-state='checked'] svg": {
        "color": "#303236",
        "fill": "#ffde34",
    },
    "&[data-state='checked']": {
        "::after": {
            "box-shadow": "inset 0px 1px 3px rgba(28, 32, 36, 0.03)",
            "outline-offset": "",
            "border-radius": "12px",
            "background": c_color("slate", 4),
            "outline": "none",
        }
    },
}
