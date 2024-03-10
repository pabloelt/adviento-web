import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color
from adviento_web.components.header_text import header_text

def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "star",
                "Patrocinado por",
                False,
            ),
            rx.chakra.span(
                "Con el apoyo de la comunidad y los patrocinadores costearé los 24 regalos. Con el apoyo de la comunidad y los patrocinadores costearé los 24 regalos.",
            ),
            rx.chakra.span(
                "¿Quieres apoyar esta iniciativa? Escríbeme a braismoure@mouredev.com o envíate algo no."
            ),
            spacing = "1",
            padding_y = Size.VERY_BIG.value,
            style = styles.max_width_style,
        ),
        bg = Color.ACCENT.value,
        width = "100%",
    )