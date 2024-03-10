import reflex as rx
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color
import adviento_web.styles.constants as constants
from adviento_web.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src = "Grinch.png",
                alt = "Imagen Pixelart Grich",
                width = Size.BIG.value,
                height = Size.BIG.value,
                ),
            rx.text("aDEViento 2024", padding_y = Size.SMALL.value),
            rx.spacer(),
            rx.hstack(
                link_icon(
                    "youtube",
                    constants.YOUTUBE_URL,
                ),
                link_icon(
                    "twitch",
                    constants.TWITCH_URL,
                ),
                link_icon(
                    "github",
                    constants.GITHUB_URL,
                ),
                padding_y = Size.SMALL.value,
                spacing = "3",
            ),
            width = "100%",
            ),
            bg = Color.PRIMARY.value,
            position = "sticky",
            border_bottom = f"0.25em solid {Color.SECONDARY.value}",
            padding_x = Size.BIG.value,
            padding_y = Size.DEFAULT.value,
            z_index = "999",
            top = "0",
            width = "100%",
    )
        