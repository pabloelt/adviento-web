import reflex as rx
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color, TextColor
import adviento_web.styles.constants as constants
import adviento_web.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2024",
            size = "7",
            padding_bottom = Size.DEFAULT.value,
            width = "100%",
            ),
        rx.flex(
            rx.image(
                src = "Grinch.png",
                alt = "imagen Avatar Grinch navideño",
                width = "16em",
                height = "16em",
                margin_right = Size.BIG.value,
                ),
            rx.vstack(
                rx.box(
                    rx.text("24 días. 24 regalos."),
                    rx.text("Del 1 al 24 de diciembre."),
                    class_name = "nes-balloon from-left is-dark",
                    ),
                rx.chakra.span(
                    "Por tercer año, ¡aquí tenéis el calendario de adviento sorpresa de nuestra ",
                    rx.chakra.span(
                        "comunidad de developers",
                        color = Color.ACCENT.value,
                        font_size = Size.DEFAULT.value,
                        ),
                        "!",
                        ),
                rx.chakra.span(
                    "Una actividad en la que sortearé un regalo relacionado con programación y desarrollo software"
                    ),
                rx.chakra.span(
                    "Una actividad en la que sortearé un regalo relacionado con programación y desarrollo software"
                    ),
                rx.link(
                    "#aDEViento2024",
                    href = constants.ADEVIENTO_URL,
                    is_external = True,
                    color = TextColor.TERCIARY.value,
                    padding_top = Size.BIG.value,
                    font_size = Size.MEDIUM.value,
                    ),
                    align_items = "start",
                ),
                flex_direction = ["column", "column", "column", "row", "row"]
            ),
        padding_top = Size.VERY_BIG.value,
        style = styles.max_width_style,
        margin_x = Size.VERY_BIG.value,
        )