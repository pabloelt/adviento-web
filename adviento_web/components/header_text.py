import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import TextColor

def header_text(icon: str, text: str, dark = True) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name = f"nes-icon is-medium {icon}",
        ),
        rx.heading(
            text,
            size = "5",
            margin_top = Size.MEDIUM.value,
            color = TextColor.ACCENT.value if dark else TextColor.SECONDARY.value,
        ),
        spacing = "6",
        padding_bottom = Size.BUTTON.value,
    )
