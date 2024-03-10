import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color, TextColor
import adviento_web.styles.constants as constants

def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de aDEViento 2024.",
                font_size = Size.MEDIUM.value,
                ),
            rx.link(
                "Creado con ",
                rx.box(class_name = "nes-icon is-small heart"),
                " love (y gracias a ti) por MourDev by Brais Moure",
                font_size = Size.MEDIUM.value,
                color = TextColor.TERCIARY.value,
                href = constants.MOUREDEV_URL,
                margin_top = Size.ZERO.value,
            ),
            align_items = "start",
        ),
        rx.spacer(),
        rx.box(
            class_name = "nes-charmander is-small",
            alt = "Logo mouredev",
        ),
        padding_bottom = Size.BIG.value,
        style = styles.max_width_style,
        align_items = "center",
    )