import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size

def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            class_name = "nes-btn is-error",
        ),
        href = url,
        is_external = True,
    )