import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color
import adviento_web.styles.constants as constants
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button
from adviento_web.components.day import day

def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario de aDEViento",
        ),
        rx.vstack(
            rx.hstack(
                rx.text("El evento comienza en"),
                rx.text(id = "countdown"),
                align_items = "start",
            ),
            button(
                "Recordar",
                constants.DISCORD_EVENT_URL,
            ),
            rx.chakra.span(
                "Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo.",
            ),
            align_items = "start",
            width = "100%",
            class_name = "nes-container is-dark with-title",
        ),
        rx.chakra.responsive_grid(
            rx.foreach(
                list(range(1,25)),
                lambda number: 
                day(
                    number,
                )
            ),
            columns = [3, 3, 4, 5, 6],
            spacing = "6",
            width = "100%",
            padding_top = Size.BIG.value,
        ),
        rx.script(src = "/js/countdown.js"),
        style = styles.max_width_style,
    )
