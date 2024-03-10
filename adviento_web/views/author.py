import reflex as rx
import datetime 
import adviento_web.styles.styles as styles
import adviento_web.styles.constants as constants
from adviento_web.styles.styles import Size, Color, TextColor
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button

def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hola, mi nombre es Pablo"
        ),
        rx.flex(
            rx.avatar(
                name = "Pabloelt",
                size = "6",
                src = "Grinch.png",
                bg = Color.PRIMARY.value,
                padding = "6",
                border = "4px",
                border_color = Color.SECONDARY.value,
                margin_right = Size.BIG.value,
                margin_bottom = Size.DEFAULT.value,
            ),
            rx.vstack(
                rx.chakra.span(f"Soy ingeniero de software desde hace más de {experience()} años."),
                rx.chakra.span(
                    "En 2018 comencé a divulgar contenido sobre programación y desarrollo de software en redes sociales como ",
                    rx.chakra.span(
                        "@mourdev",
                        color = TextColor.ACCENT.value,
                        font_size = Size.DEFAULT.value,
                        ),
                        "."
                    ),
                author_buttons(),
                width = "100%",
                align_items = "start",
                spacing = "2",
            ),
            align_items = "start",
            #spacing = "6",
            flex_direction = ["column", "column", "column", "row", "row"],        
        ),
        style = styles.max_width_style,
    )


def author_buttons() -> rx.Component:
    return rx.hstack(
        button(
            "Youtube",
            constants.YOUTUBE_URL,
        ),
        button(
            "Twitch",
            constants.TWITCH_URL,
        ),
        button(
            "Discord",
            constants.DISCORD_URL,
        ),
        spacing = "3",
    )

def experience() -> int:
    today = datetime.date.today()
    return today.year-2010